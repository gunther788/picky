
import time
import asyncio
import sys
import logging
from datetime import datetime

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.INFO)


def noop_handler(*args, **kwargs):
    pass

bot = Bot(handler=noop_handler)


async def send_message(topic, msg_id, message):
    channel = chat1.ChatChannel(name="idoruch.alerts", topic_name=topic, members_type="team")

    if msg_id > 0:
        logging.info(f"send_message({topic}, {msg_id}, edit '{message}')")
        await bot.chat.edit(channel, msg_id, message)
        return msg_id

    else:
        logging.info(f"send_message({topic}, {msg_id}, send '{message}')")
        result = await bot.chat.send(channel, message)
        return result.message_id


asyncio.run(send_message("containers", 0, "--- restarting ---"))

def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


HOSTS = {
    "ipa1.aidoru.ch": {
        "name": "ipa1.aidoru.ch",
        "messages": {
            "centos7": 0,
            "ipa": 0,
        },
        "state": "DOWN",
        "timestamp": get_timestamp(),
    },
    "plex.aidoru.ch": {
        "name": "plex.aidoru.ch",
        "messages": {
            "containers": 0,
        },
        "state": "UP",
        "timestamp": get_timestamp(),
    },
    "foreman.aidoru.ch": {
        "name": "foreman.aidoru.ch",
        "messages": {
            "centos7": 0,
            "foreman": 0,
        },
        "state": "UP",
        "timestamp": get_timestamp(),
    },
}

CHANNELS = {
    "containers": get_timestamp(),
    "gold": get_timestamp(),
}
