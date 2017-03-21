from Program import discord,asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ',client.user.name,'(',client.user.id,')')

@client.event
async def on_message(message):
    print(message)

client.run('E78l1UAmbc47wUEpqn0V6Km8fmGploz5')

# URL to add:
#   (Malul):  https://discordapp.com/api/oauth2/authorize?client_id=293837616787488780&scope=bot&permissions=0
#   (Zafig):  https://discordapp.com/api/oauth2/authorize?client_id=&scope=bot&permissions=0
#   (Fknfgt): https://discordapp.com/api/oauth2/authorize?client_id=&scope=bot&permissions=0
#   (John):   https://discordapp.com/api/oauth2/authorize?client_id=&scope=bot&permissions=0