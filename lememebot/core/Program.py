import discord
import asyncio
from Token import get_discord_token

print('')
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ',client.user.name,'(',client.user.id,')')

@client.event
async def on_message(message):
    if (message.author.id != client.user.id):
        if('!!quit' == message.content):
            await client.logout()
        else:
            print('[DEBUG] ',message.author,': ', message.content)
        #await client.send_message(message.channel, 'Calculating messages...')

client.run(get_discord_token())

# URL to add:
#   (Malul):  https://discordapp.com/api/oauth2/authorize?client_id=294886929735090186&scope=bot&permissions=0
#   (Zafig):  https://discordapp.com/api/oauth2/authorize?client_id=*DUMMY*&scope=bot&permissions=0
#   (Fknfgt): https://discordapp.com/api/oauth2/authorize?client_id=294883627165024258&scope=bot&permissions=0
#   (John):   https://discordapp.com/api/oauth2/authorize?client_id=*DUMMY*&scope=bot&permissions=0

# Tokens:
#   (Malul):  rUVg8F4locEucRGuTSKkPX2R6qX4ycZO
#   (Zafig):  MjkzMDk1NzY0MDEwMzM2MjY2.C7bqXA.QjOGFq-bP409lsLH6T7TNzS1LgQgit
#   (Fknfgt): Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0
#   (John):   TODO
