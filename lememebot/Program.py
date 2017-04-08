#!/usr/bin/python
# -*- coding: utf-8 -*-

import discord
import sys
import asyncio
import threading
import logging

from Token import get_discord_token
from handlers.Cleverbot import on_message as clv_handle
from handlers.HoferHandler import on_message as hofer_handle
from handlers.Overwatch import on_message as overwatch_handle
from handlers.remindMe import on_message as remindme_handle
from handlers.Pasta import PastaBot
from handlers.RunGameBeta import RunGameBeta

if not(__name__ == "__main__" and len(sys.argv) > 1):
    print('Missing username argument. USAGE: Program.py <username>')
    exit(0)

logging.basicConfig(filename='root.log',
                    level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

client = discord.Client()

handlers = [hofer_handle,
            overwatch_handle,
            remindme_handle,
            clv_handle,
            PastaBot(client).on_message,
            RunGameBeta().on_message]


@client.event
async def on_ready():
    logging.info('Logged in as ' + client.user.name + ' (' + client.user.id + ')')
    print('Logged in as ',client.user.name,'(',client.user.id,')')


@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if '!!quit' == message.content:
            await client.logout()
        else:
            logging.info(message.author.name + ': ' + message.content)
            print('[DEBUG: Main] ', message.author, ': ', message.content)
            # call all handlers with client and message
            for handle in handlers:
                await handle(client=client, message=message)

@client.event
async def on_member_update(before, after):

    msg = after.name

    if after.game:
        msg += ' started playing ' + after.game.name + '!'
    elif before.game:
        msg += ' stopped playing ' + before.game.name + '!'
    elif before.status.value == 'offline':
        msg += ' came online!'
    elif after.status.value == 'offline':
        msg += ' went offline!'
    else:
        msg += ' went from ' + before.status.value + ' to ' + after.status.value + '!'

    await client.send_message(destination=after.server.default_channel, content=msg)

client.run(get_discord_token(sys.argv[1]))
