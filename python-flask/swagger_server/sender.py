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


async def send_message(topic, msg_id, message):
    channel = chat1.ChatChannel(name=CONFIG['keybase']['TEAM'], topic_name=topic, members_type="team")

    if msg_id > 0:
        app.logger.info(f"send_message('{topic}', {msg_id}, edit '{message}')")
        await bot.chat.edit(channel, msg_id, message)
        return msg_id

    else:
        app.logger.info(f"send_message('{topic}', {msg_id}, send '{message}')")
        result = await bot.chat.send(channel, message)
        return result.message_id


def hosts_notify(key):
    """Take a host from HOSTS and iterate over its messages dict
    and notify each known channel.
    """
    host = HOSTS[key]
    app.logger.info(f"hosts_notify('{host.name}') in channel {host.channel}")

    # let's see if there is a message we should update
    if host.msg_id > 0:

        try:
            # update the message in place
            asyncio.run(send_message(host.channel, host.msg_id, host.picky))
            app.logger.info(f"message had id {host.msg_id}")

        except Exception as exc:
            # someone may have deleted the message by now, so let's start
            # a new one
            host.msg_id = asyncio.run(send_message(host.channel, 0, host.picky))
            app.logger.info(f"new message has id {host.msg_id} (recovered from {exc})")

    else:
        # same as above, there's no message so we start a new one
        host.msg_id = asyncio.run(send_message(host.channel, 0, host.picky))
        app.logger.info(f"new message has id {host.msg_id}")

    # we've recovered, so it's time to reset the state to 0 and start
    # new messages should there be any more
    if host.all_good:
        host.msg_id = 0
