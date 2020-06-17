#!/usr/bin/env python3

import time
import asyncio
import sys
import logging

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)

def noop_handler(*args, **kwargs):
    pass

bot = Bot(handler=noop_handler)

async def send_message(topic, msg_id, message):
    channel = chat1.ChatChannel(name="idoruch.alerts", topic_name=topic, members_type="team")

    if msg_id > 0:
        await bot.chat.edit(channel, msg_id, message)

    else:
        result = await bot.chat.send(channel, message)
        return result.message_id

logging.debug("new message")
msg_id = asyncio.run(send_message("containers", 0, "🟨 message to containers channel"))
logging.debug(f"new message has id {msg_id}")
time.sleep(4)
logging.debug(f"editing message id {msg_id}")
asyncio.run(send_message("containers", msg_id, "🟥 edited message to containers channel"))
time.sleep(4)
logging.debug(f"deleting message id {msg_id}")
asyncio.run(send_message("containers", msg_id, "🟩 all ok in containers channel"))
logging.debug(f"deleted message id {msg_id}")
time.sleep(4)
