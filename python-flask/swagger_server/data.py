
import time
import asyncio
import sys
import logging
from datetime import datetime

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

from swagger_server.models.host import Host
from swagger_server.models.channel import Channel

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


def get_timestamp():
    return datetime.utcnow().strftime(("%Y-%m-%d %H:%M:%SZ"))


HOSTS = {
    "ipa1.aidoru.ch": Host.from_dict({
        "name": "ipa1.aidoru.ch",
        "messages": {
            "centos7": 0,
            "ipa": 0,
        },
        "state": "DOWN",
        "timestamp": get_timestamp(),
    }),
    "plex.aidoru.ch": Host.from_dict({
        "name": "plex.aidoru.ch",
        "messages": {
            "containers": 0,
        },
        "state": "UP",
        "timestamp": get_timestamp(),
    }),
    "foreman.aidoru.ch": Host.from_dict({
        "name": "foreman.aidoru.ch",
        "messages": {
            "centos7": 0,
            "foreman": 0,
        },
        "state": "UP",
        "timestamp": get_timestamp(),
    }),
}


CHANNELS = {
    "containers": Channel.from_dict({
        "name": "containers",
        "timestamp": get_timestamp(),
    }),
    "gold": Channel.from_dict({
        "name": "gold",
        "timestamp": get_timestamp(),
    }),
    "silver": Channel.from_dict({
        "name": "silver",
        "timestamp": get_timestamp(),
    })
}
