from flask import Flask
app = Flask(__name__)

import asyncio
import yaml

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

from swagger_server.data import CONFIG, DATA
from swagger_server.models.host import Host


def noop_handler(*args, **kwargs):
    pass

bot = Bot(handler=noop_handler)


async def async_send(topic, message, msg_id=0):
    channel = chat1.ChatChannel(name=CONFIG['keybase']['TEAM'], topic_name=topic, members_type="team")

    if msg_id > 0:
        app.logger.info(f"async_send('{topic}', {msg_id}, edit '{message}')")
        await bot.chat.edit(channel, msg_id, message)
        return msg_id

    else:
        app.logger.info(f"async_send('{topic}', {msg_id}, send '{message}')")
        result = await bot.chat.send(channel, message)
        return result.message_id


def send(topic, message, msg_id=0):
    # let's see if there is a message we should update
    if msg_id > 0:

        try:
            # update the message in place
            asyncio.run(async_send(topic, message, msg_id))

        except Exception as exc:
            # someone may have deleted the message by now, so let's start
            # a new one
            msg_id = asyncio.run(async_send(topic, message))

    else:
        # same as above, there's no message so we start a new one
        msg_id = asyncio.run(async_send(topic, message))

    return msg_id
