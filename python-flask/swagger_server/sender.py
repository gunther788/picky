from flask import Flask
app = Flask(__name__)

import asyncio
import yaml

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

from swagger_server.data import CONFIG, HOSTS, CHANNELS
from swagger_server.models.host import Host
from swagger_server.models.channel import Channel

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


def channels_notify(name):
    """Take a channel from CHANNELS and make sure it is up and running.
    """
    app.logger.info(f"channels_notify('{name}')")
    if name is not None and name in CHANNELS:
        asyncio.run(send_message(name, 0, "Welcome to the Machine!"))


def hosts_notify(name):
    """Take a host from HOSTS and iterate over its messages dict
    and notify each known channel.
    """
    app.logger.info(f"hosts_notify('{name}')")
    if name is not None and name in HOSTS:
        host = HOSTS[name]
        app.logger.info(f"hosts_notify('{name}') has {host.messages}")

        for channel in CHANNELS:
            app.logger.info(f"hosts_notify checking '{channel}'")

            if channel in host.messages:
                app.logger.info(f"hosts_notify '{channel}' matches {host.messages}")

                # let's see if there is a message we should update
                msg_id = host.messages[channel]
                if msg_id > 0:

                    try:
                        # update the message in place
                        asyncio.run(send_message(channel, msg_id, host.picky.replace('\n', ' ')))
                        app.logger.info(f"message had id {msg_id}")

                    except Exception as exc:
                        # someone may have deleted the message by now, so let's start
                        # a new one
                        msg_id = asyncio.run(send_message(channel, 0, host.picky.replace('\n', ' ')))
                        HOSTS[name].messages[channel] = msg_id
                        app.logger.info(f"new message has id {msg_id} (recovered from {exc})")

                else:
                    # same as above, there's no message so we start a new one
                    msg_id = asyncio.run(send_message(channel, 0, host.picky.replace('\n', ' ')))
                    HOSTS[name].messages[channel] = msg_id
                    app.logger.info(f"new message has id {msg_id}")

                # we've recovered, so it's time to reset the state to 0 and start
                # new messages should there be any more
                if HOSTS[name].all_good:
                    HOSTS[name].messages[channel] = 0
