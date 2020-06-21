from flask import Flask
app = Flask(__name__)

from datetime import datetime
import configparser
import yaml

from swagger_server.models.channel import Channel
from swagger_server.models.host import Host
from swagger_server.models.service import Service

CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")
app.logger.info("read '/data/picky.ini'")

def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


HOSTS = {
    "ipa1.aidoru.ch": Host.from_dict({
        "name": "ipa1.aidoru.ch",
        "messages": {
            "centos7": 0,
            "ipa": 0,
        },
        "state": "DOWN",
        "output": "CRITICAL - Host Unreachable",
        "timestamp": get_timestamp(),
    }),
    "plex.aidoru.ch": Host.from_dict({
        "name": "plex.aidoru.ch",
        "messages": {
            "containers": 0,
        },
        "state": "UP",
        "output": "all good",
        "timestamp": get_timestamp(),
    }),
    "foreman.aidoru.ch": Host.from_dict({
        "name": "foreman.aidoru.ch",
        "messages": {
            "centos7": 0,
            "foreman": 0,
        },
        "state": "UP",
        "output": "all good",
        "timestamp": get_timestamp(),
    }),
}


CHANNELS = {
    "containers": Channel.from_dict({
        "name": "containers",
        "timestamp": get_timestamp(),
    }),
    "gold": Channel.from_dict({
        "name": "gold",
        "timestamp": get_timestamp(),
    }),
    "silver": Channel.from_dict({
        "name": "silver",
        "timestamp": get_timestamp(),
    })
}


with open('/data/cache.yml', 'w') as file:
    yaml.dump({'CHANNELS': CHANNELS}, file, explicit_start=True)
