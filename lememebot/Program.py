import discord
import sys
import asyncio
import threading

from Token import get_discord_token
from handlers.Cleverbot import on_message as clv_handle
from handlers.HoferHandler import on_message as hofer_handle
from handlers.Overwatch import on_message as overwatch_handle
from handlers.remindMe import on_message as remindme_handle
from handlers.Pasta import PastaBot

if not(__name__ == "__main__" and len(sys.argv) > 1):
    print('Missing username argument. USAGE: Program.py <username>')
    exit(0)

client = discord.Client()

handlers = [hofer_handle,
            overwatch_handle,
            remindme_handle,
            clv_handle,
            PastaBot(client).on_message]


@client.event
async def on_ready():
    print('Logged in as ',client.user.name,'(',client.user.id,')')


@asyncio.coroutine
def on_message_DoWork(message):
    for i in range(0, len(handlers)):
        yield from handlers[i](client, message)


@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if '!!quit' == message.content:
            await client.logout()
        else:
            print('[DEBUG: Main] ', message.author, ': ', message.content)
            # call all handlers with client and message
            for handle in handlers:
                #loop = asyncio.get_event_loop()
                #loop.create_task(handle.on_message(client, message))
                await handle(client=client, message=message)

client.run(get_discord_token(sys.argv[1]))
