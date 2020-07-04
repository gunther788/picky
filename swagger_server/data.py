
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

    # state transitions
    'OK-WARNING': ':down-yellow-triangle:',
    'UP-DOWN': ':down-red-triangle:',
    'OK-CRITICAL': ':down-red-triangle:',
    'WARNING-CRITICAL': ':down-red-triangle:',
    'CRITICAL-WARNING': ':up-yellow-triangle:',
    'DOWN-UP': ':up-green-triangle:',
    'WARNING-OK': ':up-green-triangle:',
    'CRITICAL-OK': ':up-green-triangle:',
    
    # repeat messages
    'bell': '🔔',
}
