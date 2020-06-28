
import configparser
CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")

# set of channels with hosts and their services
from swagger_server.models.channel import Channel
DATA = {}

from swagger_server.controllers.channels_controller import alerts_channel

alerts_channel("gold", {"name": "gold"})
alerts_channel("silver", {"name": "silver"})
