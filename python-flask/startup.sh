#!/bin/sh

# load environment
export $(grep -v '^#' /data/picky.cfg | xargs)
sleep 5

# ping test
keybase ping
sleep 10

# and let's go!
exec python3 -m swagger_server
