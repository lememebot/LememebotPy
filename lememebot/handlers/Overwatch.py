import asyncio

#commands = [('hello',on_cmd_hello)]

# will tell dean to shut the fuck up when he goes nuts
@asyncio.coroutine
async def on_message(client,message):
    print('Hey')
