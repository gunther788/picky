import connexion
import six

from swagger_server.models.channel import Channel
from swagger_server.models.host import Host
from swagger_server.models.service import Service

from swagger_server.data import DATA, CONFIG, EMOJI
from swagger_server.sender import send

from flask import Flask, make_response, abort
app = Flask(__name__)


from datetime import datetime


def limit_timestamps(timestamps):
    if len(timestamps) < 6:
        return timestamps

    return [ timestamps[0], '...' ] + timestamps[-3:]


def amend_host_timestamps(timestamps=[], before='UP', after='UP'):
    if timestamps == []:
        t = "%Y-%m-%d %H:%M:%SZ"
    else:
        t = "%H:%M:%SZ"
    if before == after:
        return timestamps
    return limit_timestamps(timestamps + [ datetime.utcnow().strftime(t) + EMOJI[f"{before}-{after}"] ])


def amend_service_timestamps(timestamps=[], before='OK', after='OK'):
    if before == after:
        return timestamps
    return limit_timestamps(timestamps + [ datetime.utcnow().strftime("%H:%M:%SZ") + EMOJI[f"{before}-{after}"] ])


def get_channels():
    """
    Get all Channel objects, the top-level data set.
    """
    app.logger.info(f"get_channels()")
    return [DATA[key] for key in sorted(DATA.keys())]


def reset_channels():
    """
    Reset all Channel objects.
    """
    app.logger.info(f"reset_channels()")
    for key in list(DATA.keys()):
        del DATA[key]
    return []


def put_channel(channel, body={}):
    """
    Request a new channel to be created in Keybase, if required, by simply
    posting a welcome message in a new channel.
    """
    app.logger.info(f"put_channel({channel}, {body})")
    if channel not in DATA:
        DATA[channel] = Channel.from_dict({
            'name': channel,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}",
            'hosts': {},
        })
        ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
        send(channel, f"\n\n\n{EMOJI['star'] * 5}\nAlerts begin at *{ts}*\n{EMOJI['star'] * 5}\n")

    return DATA[channel]


def get_hosts(channel):
    """
    Get a host entry if it exists in that channel data.
    """
    app.logger.info(f"get_hosts({channel})")
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    h = DATA[channel].hosts
    return [h[key] for key in sorted(h.keys())]


def all_good(h):
    """
    Return True iff the host and all services are at state = UP / OK.
    """
    if h.state != "UP":
        return False

    for s in h.services:
        if h.services[s].state != "OK":
            return False

    return True


def format_host(h):
    """
    Format the host entry for posting to Keybase / save at host.picky
    """
    app.logger.debug(f"format_host({h})")
    msg = []

    if h.state in EMOJI:
        msg.append(EMOJI[h.state])

    # for now skip the sla's
    # if h.sla in EMOJI:
    #     msg.append(EMOJI[h.sla])

    msg.append(h.name)

    msg.append(f"({' '.join(h.timestamps)})")

    msg.append(f"\n{CONFIG['picky']['HOSTURL']}={h.name}")

    if h.state != 'UP' and h.output is not None and h.output != "":
        msg.append(f"\n`{h.output}`")

    return ' '.join(msg)


def init_host(channel, host, body=Host.from_dict({})):
    """
    Make sure the host object exists, either by creating a proper entry
    via put_host() or indirectly by put_service().
    """
    app.logger.info(f"init_host({channel}, {host}, {body})")
    c = put_channel(channel)
    if host not in c.hosts:
        c.hosts[host] = Host.from_dict({
            'name': host,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}",
            'timestamps': [],
            'services': {},
        })
    return c.hosts[host]


def put_host(channel, host, body=Host.from_dict({})):
    """
    Main entry point for adding host alerts, called from hosts_controller.put_host().
    """
    app.logger.info(f"put_host({channel}, {host}, {body})")

    h = init_host(channel, host, body)

    # update timestamps and transitions
    h.timestamps = amend_host_timestamps(h.timestamps, h.state, body.state)

    # if we have a state, save it
    if body.state:
        h.state = body.state

    # if there's output, save it (but only render it if state != OK)
    if body.output:
        h.output = body.output

    # if there are service, append them, but usually we get separate put_service() calls
    if body.services:
        h.services = body.services

    # save the SLA (unused at the moment)
    if body.sla:
        h.sla = body.sla

    # this will likely be "Problem" only - "Acknowledgement" isn't processed yet
    if body.note_type:
        h.note_type = body.note_type

    # notify Keybase channel and overwrite previous entry, if any
    send_host(channel, host)

    # if all is well, the next message should be renderered as a new alert
    if all_good(h):
        h.msg_id = 0
        h.timestamps = []

    return h


def send_host(channel, host):
    """
    Format the host, append services that are not well, and notify Keybase
    """
    app.logger.debug(f"send_host({channel}, {host})")
    h = DATA[channel].hosts[host]
    h.picky = format_host(h)
    msg = [ h.picky ]

    # no point telling us about failed services when the host is down
    # and no point telling us about running services when everything is well
    if not all_good(h) and h.state == "UP":
        for service in h.services:
            s = h.services[service]
            s.picky = format_service(s)
            msg.append(s.picky)

    h.msg_id = send(channel, '\n'.join(msg), h.msg_id)


def get_services(channel, host):
    """
    Get a list of all services of a host in a channel
    """
    app.logger.info(f"get_services({channel}, {host})")
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    if host not in DATA[channel].hosts:
        return make_response(f"Host {host} not found", 404)

    s = DATA[channel].hosts[host].services
    return [s[key] for key in sorted(s.keys())]


def format_service(s):
    """
    Very similar to format_host(), just on a service level
    """
    app.logger.info(f"format_service({s})")
    msg = []
    if s.state in EMOJI:
        msg.append(EMOJI[s.state])

    # for now skip the sla's
    # if s.sla in EMOJI:
    #     msg.append(EMOJI[s.sla])

    msg.append(s.name)

    msg.append(f"({' '.join(s.timestamps)})")

    if s.state != 'OK' and s.output is not None and s.output != "":
        msg.append(f"\n`{s.output}`")

    return ' '.join(msg)


def init_service(channel, host, service, body=Host.from_dict({})):
    """
    Make sure the service object exists
    """
    app.logger.info(f"init_service({channel}, {host}, {service}, {body})")
    h = init_host(channel, host)
    
    if service not in h.services:
        h.services[service] = Service.from_dict({
            'name': service,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}/{service}",
            'timestamps': [],
            'services': {},
        })

        if h.timestamps == []:
            h.timestamps = [ datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ") ]

    return h.services[service]


def put_service(channel, host, service, body=Service.from_dict({})):
    """
    Main entry point for a service-level alert, and will generate a host entry
    if it doesn't exist yet.
    """
    app.logger.info(f"put_service({channel}, {host}, {service}, {body})")
    s = init_service(channel, host, service, body)

    s.timestamps = amend_service_timestamps(s.timestamps, s.state, body.state)
        
    if body.state:
        s.state = body.state

    if body.output:
        s.output = body.output

    if body.sla:
        s.sla = body.sla

    # remember that service alerts should also create host entries in the channel,
    # so we simply call send_host() and have it render the rest as needed
    send_host(channel, host)

    return s
