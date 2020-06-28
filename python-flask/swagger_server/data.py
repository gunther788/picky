
import configparser
CONFIG = configparser.SafeConfigParser()
CONFIG.read("/data/picky.ini")

# set of channels with hosts and their services
DATA = {}
