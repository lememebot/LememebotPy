import discord
import sys
import asyncio
import threading

from Token import get_discord_token
from handlers.Cleverbot import on_message as clv_handle
from handlers.HoferHandler import on_message as hofer_handle
from handlers.Overwatch import on_message as overwatch_handle
from handlers.remindMe import on_message as remindme_handle

if not(__name__ == "__main__" and len(sys.argv) > 1):
    print('Missing username argument. USAGE: Program.py <username>')
    exit(0)

client = discord.Client()
handlers = [hofer_handle,
            overwatch_handle,
            remindme_handle,
            clv_handle]

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
            print('[DEBUG] ',message.author,': ', message.content)
            # call all handlers with client and message

            loop = asyncio.get_event_loop()
            #try:
            loop.run_until_complete(await on_message_DoWork(message))
            #except:
            #    loop.run_until_complete(client.logout())
            #finally:
                #loop.close()

client.run(get_discord_token(sys.argv[1]))
# URL to add:
#   (Malul):  https://discordapp.com/api/oauth2/authorize?client_id=294886929735090186&scope=bot&permissions=0
#   (Zafig):  https://discordapp.com/api/oauth2/authorize?client_id=*DUMMY*&scope=bot&permissions=0
#   (Fknfgt): https://discordapp.com/api/oauth2/authorize?client_id=294883627165024258&scope=bot&permissions=0
#   (John):   https://discordapp.com/api/oauth2/authorize?client_id=294887096236245002&scope=bot&permissions=0

# Tokens:
#   (Malul):  rUVg8F4locEucRGuTSKkPX2R6qX4ycZO
#   (Zafig):  MjkzMDk1NzY0MDEwMzM2MjY2.C7bqXA.QjOGFq-bP409lsLH6T7TNzS1LgQgit
#   (Fknfgt): Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0
#   (John):   Mjk0ODg3MDk2MjM2MjQ1MDAy.C7_x1A.30PGWlcc6gedyiN-EGKl1AAGbR4
