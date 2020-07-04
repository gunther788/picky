#!/bin/sh

# load environment
export $(grep -v '^#' /data/picky.ini | tr -d ' ' | grep "=" | xargs)
sleep $(expr 1 \* $DELAY)

# ping test
keybase ping
sleep $(expr 3 \* $DELAY)

# send a test message
#keybase --debug chat send --channel "" ${TEAM} "PICKY reconnecting at $(date)"
#sleep $(expr 2 \* $DELAY)

# and let's go!
exec python3 -m swagger_server
