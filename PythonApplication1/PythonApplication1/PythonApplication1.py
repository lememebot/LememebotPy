import discord
import asyncio
from PythonApplication1 import discord, asyncio

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
client = discord.Client()

class Voice(object):
    voice = 'a'

    def __init__(self):
        self.voice = 'b'

    @classmethod
    def is_connected(self,server):
        if self.voice is None or not client.is_voice_connected(server):
            return False
        else:
            return True

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    emjs = client.get_all_emojis()
    if message.content.lower().startswith('!myman'):
        str = '{} {} {}'.format('Right back at you', message.author.mention, 'My man!')
        if 'guy' in message.author.display_name:
            str = '{} {}'.format(str, ':heart_eyes:')
        elif 'John' in message.author.display_name:
            str = '{} {}'.format(str, ':muscle:')
        elif 'fag' in message.author.display_name:
            str = '{} {}'.format(str, ':gay_pride_flag:')
        await client.send_message(message.channel, str)
    elif message.content.lower().startswith('!gay'):
        if not Voice.is_connected(message.author.server):
            Voice.voice = await client.join_voice_channel(message.author.voice.voice_channel) # check if user is in channel
        #if not client.is_voice_connected(message.author.server):
            #voice = await client.join_voice_channel(message.author.voice.voice_channel) # check if user is in channel
        player = Voice.voice.create_ffmpeg_player('gay.mp3')
        player.start();
        #await voice.disconnect()

client.run('Mjg1MDAwNjIyMDQwNjc4NDAx.C5NzRw.RxxdnfbeWGtb2uGlhUaBDsHOID0')    

