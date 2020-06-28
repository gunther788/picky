import connexion
import six

from swagger_server.models.channel import Channel
from swagger_server.models.host import Host
from swagger_server.models.service import Service

from swagger_server.data import DATA, CONFIG
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


def put_host(channel, host, body={}):
    c = put_channel(channel)
    if host not in c.hosts:
        c.hosts[host] = Host.from_dict({
            'name': host,
            'url': f"{CONFIG['picky']['BASEURL']}/{channel}/{host}",
            'timestamp': get_timestamp(),
            'services': {},
        })

    h = c.hosts[host]
    h.timestamp = get_timestamp()
    send(channel, f":: {h.timestamp} {h.host}")
    return c.hosts[host]
