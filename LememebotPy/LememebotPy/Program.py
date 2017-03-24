import discord,asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ',client.user.name,'(',client.user.id,')')

@client.event
async def on_message(message):
    print(message)

client.run('Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0')

# URL to add:
#   (Malul):  https://discordapp.com/api/oauth2/authorize?client_id=293837616787488780&scope=bot&permissions=0
#   (Zafig):  https://discordapp.com/api/oauth2/authorize?client_id=*DUMMY*&scope=bot&permissions=0
#   (Fknfgt): https://discordapp.com/api/oauth2/authorize?client_id=294883627165024258&scope=bot&permissions=0
#   (John):   https://discordapp.com/api/oauth2/authorize?client_id=*DUMMY*&scope=bot&permissions=0

# TOKEN IDS:
#   (Malul):  https://discordapp.com/api/oauth2/authorize?client_id=293837616787488780&scope=bot&permissions=0
#   (Zafig):  TODO
#   (Fknfgt): Mjk0ODgzNjI3MTY1MDI0MjU4.C7bnWA.T466dvvu3Z0cssV7tuBgfffGRb0
#   (John):   TODO
