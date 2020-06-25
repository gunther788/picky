from flask import Flask
app = Flask(__name__)

from datetime import datetime
import configparser
import yaml

from swagger_server.models.host import Host
from swagger_server.models.service import Service


CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")
app.logger.info("read /data/picky.ini")


def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


HOSTS = {
    "ipa1.aidoru.ch/gold": Host.from_dict({
        "name": "ipa1.aidoru.ch",
        "channel": "gold",
        "msg_id": 0,
        "state": "DOWN",
        "output": "CRITICAL - Host Unreachable",
        "timestamp": get_timestamp(),
    }),
    "plex.aidoru.ch/silver": Host.from_dict({
        "name": "plex.aidoru.ch",
        "channel": "silver",
        "msg_id": 0,
        "state": "UP",
        "output": "all good",
        "timestamp": get_timestamp(),
    }),
    "foreman.aidoru.ch/silver": Host.from_dict({
        "name": "foreman.aidoru.ch",
        "channel": "silver",
        "msg_id": 0,
        "state": "UP",
        "output": "all good",
        "timestamp": get_timestamp(),
    }),
}
