from cleverwrap import CleverWrap
import asyncio

CLEVERBOT_COMMAND = "!cleverbot ";
# will tell dean to shut the fuck up when he goes nuts
@asyncio.coroutine
async def on_message(client, message):
    print ("YES")
    if (message.content.startswith(CLEVERBOT_COMMAND)):
        cw = CleverWrap("CC1cx7eaidCi0tvh7RfyC7eoYkA")
        clvrbot_msg_cnt = message.content.split(CLEVERBOT_COMMAND)[1]
        print ("Calling Cleverbot with " + clvrbot_msg_cnt + "...")
        answer = cw.say(clvrbot_msg_cnt)
        print(answer)
        await client.send_message(destination=message.channel, content=answer)
        #"Hello Human."
        cw.reset() # resets the conversation ID and conversation state.
