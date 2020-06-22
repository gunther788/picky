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
app.logger.info("read /data/picky.ini")


def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


channelfile = '/data/channels.yml'

def save_channels():
    with open(channelfile, 'w') as file:
        yaml.dump(CHANNELS, file, explicit_start=True)
        app.logger.info(f"wrote {channelfile}")

def load_channels():
    with open(channelfile, 'r') as file:
        return yaml.full_load(file)
        app.logger.info(f"read {channelfile}, got {CHANNELS}")

CHANNELS = load_channels()

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
