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
    return [DATA[key] for key in sorted(DATA.keys())]


def put_channel(channel, body={}):
    if channel not in DATA:
        DATA[channel] = Channel.from_dict({
            'name': channel,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}",
            'timestamp': get_timestamp(),
            'hosts': {},
        })
        send(channel, ':Large Purple Square: ' + get_timestamp() + ' Welcome to the Machine!')

    return DATA[channel]


def get_hosts(channel):
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    h = DATA[channel].hosts
    return [h[key] for key in sorted(h.keys())]


def format_host(h):
    msg = []

    if h.state in EMOJI:
        msg.append(EMOJI[h.state])

    msg.append(h.timestamp)
    msg.append(h.name)

    if h.state != 'UP' and h.output is not None and h.output != "":
        msg.append(f"\n`{h.output}`")

    return ' '.join(msg)


def put_host(channel, host, body={}):
    c = put_channel(channel)
    if host not in c.hosts:
        h = Host.from_dict({
            'name': host,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}",
            'timestamp': get_timestamp(),
            'services': {},
        })

    else:
        h = c.hosts[host]

    h.timestamp = get_timestamp()
    h.picky = format_host(h)
    send(channel, h.picky)
    return h


def get_services(channel, host):
    if channel not in DATA:
        return make_response(f"Channel {channel} not found", 404)

    if host not in DATA[channel].hosts:
        return make_response(f"Host {host} not found", 404)

    s = DATA[channel].hosts[host]
    return [s[key] for key in sorted(s.keys())]


def format_service(s):
    msg = []
    if s.state in EMOJI:
        msg.append(EMOJI[s.state])

    if s.sla in EMOJI:
        msg.append(EMOJI[s.sla])

    s.append(s.name)

    if s.state != 'OK' and s.output is not None and s.output != "":
        msg.append(f"\n`{s.output}`")

    return ' '.join(msg)


def put_service(channel, host, service, body={}):
    h = put_host(channel, host)

    if service not in h.services:
        s = Service.from_dict({
            'name': service,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}/{service}",
            'timestamp': get_timestamp(),
            'services': {},
        })

    s.timestamp = get_timestamp()
    s.picky = format_service(s)
    send(channel, s.picky)
    return s
