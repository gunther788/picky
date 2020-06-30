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
def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


def get_channels():
    app.logger.info(f"get_channels()")
    return [DATA[key] for key in sorted(DATA.keys())]


def put_channel(channel, body={}):
    app.logger.info(f"put_channel({channel}, {body})")
    if channel not in DATA:
        DATA[channel] = Channel.from_dict({
            'name': channel,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}",
            'timestamp': get_timestamp(),
            'hosts': {},
        })
        send(channel, f"{EMOJI['star']} {DATA[channel].timestamp} Welcome to the Machine!")

    return DATA[channel]


def get_hosts(channel):
    app.logger.info(f"get_hosts({channel})")
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    h = DATA[channel].hosts
    return [h[key] for key in sorted(h.keys())]


def all_good(h):
    if h.state != "UP":
        return False

    for s in h.services:
        if h.services[s].state != "OK":
            return False

    return True


def format_host(h):
    app.logger.debug(f"format_host({h})")
    msg = []

    if h.state in EMOJI:
        msg.append(EMOJI[h.state])

    # for now skip the sla's
    # if h.sla in EMOJI:
    #     msg.append(EMOJI[h.sla])

    msg.append(h.name)

    if h.updates > 0:
        msg.append(f"({h.timestamp} {EMOJI['bell'] * h.updates})")

    else:
        msg.append(f"({h.timestamp})")

    if h.state != 'UP' and h.output is not None and h.output != "":
        msg.append(f"\n`{h.output}`")

    return ' '.join(msg)


def init_host(channel, host, body=Host.from_dict({})):
    app.logger.info(f"init_host({channel}, {host}, {body})")
    c = put_channel(channel)
    if host not in c.hosts:
        c.hosts[host] = Host.from_dict({
            'name': host,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}",
            'timestamp': get_timestamp(),
            'services': {},
        })
    return c.hosts[host]


def put_host(channel, host, body=Host.from_dict({})):
    app.logger.info(f"put_host({channel}, {host}, {body})")

    h = init_host(channel, host, body)

    if body.state:
        h.state = body.state
        if all_good(h):
            h.updates = 0

    if body.output:
        h.output = body.output

    if body.services:
        h.services = body.services

    if body.sla:
        h.sla = body.sla

    if body.note_type:
        h.note_type = body.note_type

    h.timestamp = get_timestamp()

    send_host(channel, host)

    if all_good(h):
        h.msg_id = 0

    elif h.updates < 6:
        h.updates += 1

    return h


def send_host(channel, host):
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
    app.logger.info(f"get_services({channel}, {host})")
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    if host not in DATA[channel].hosts:
        return make_response(f"Host {host} not found", 404)

    s = DATA[channel].hosts[host]
    return [s[key] for key in sorted(s.keys())]


def format_service(s):
    app.logger.info(f"format_service({s})")
    msg = []
    if s.state in EMOJI:
        msg.append(EMOJI[s.state])

    # for now skip the sla's
    # if s.sla in EMOJI:
    #     msg.append(EMOJI[s.sla])

    msg.append(s.name)

    if s.updates > 0:
        msg.append(f"{EMOJI['bell'] * s.updates}")

    if s.state != 'OK' and s.output is not None and s.output != "":
        msg.append(f"\n`{s.output}`")

    return ' '.join(msg)


def put_service(channel, host, service, body=Service.from_dict({})):
    app.logger.info(f"put_service({channel}, {host}, {service}, {body})")
    h = init_host(channel, host)
    
    if service not in h.services:
        h.services[service] = Service.from_dict({
            'name': service,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}/{service}",
            'timestamp': get_timestamp(),
            'services': {},
        })

    s = h.services[service]

    if body.state:
        s.state = body.state
        if s.state == "OK":
            s.updates = 0

    if body.output:
        s.output = body.output

    if body.sla:
        s.sla = body.sla

    s.timestamp = get_timestamp()

    send_host(channel, host)

    if s.state != "OK" and s.updates < 6:
        s.updates += 1

    return s
