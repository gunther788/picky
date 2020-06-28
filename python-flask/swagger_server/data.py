
import configparser
CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")

# set of channels with hosts and their services
from swagger_server.models.channel import Channel
DATA = {

    "gold": Channel.from_dict({
        "name": "gold",
    }),
    "silver": Channel.from_dict({
        "name": "silver",
    }),

}
