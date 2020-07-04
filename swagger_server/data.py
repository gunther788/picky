
import configparser
CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")

# set of channels with hosts and their services
DATA = {}


EMOJI = {
    # channels
    'star': '⭐',

    # sla
    'gold': '🥇',
    'silver': '🥈',
    'bronze': '🥉',

    # host state
    'UP': '🟩',
    'DOWN': '🟥',

    # service state
    'OK': '🟢',
    'WARNING': '🟡',
    'CRITICAL': '🔴',
    'UNKNOWN': '🟣',

    # repeat messages
    'bell': '🔔',
}
