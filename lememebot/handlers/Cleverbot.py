<<<<<<< Updated upstream

=======
from cleverwrap import CleverWrap
>>>>>>> Stashed changes

CLEVERBOT_COMMAND = "!cleverbot ";
# will tell dean to shut the fuck up when he goes nuts
<<<<<<< Updated upstream
def on_message(client, message):
    if (message.content.startswith(CLEVERBOT_COMMAND)):
        cw = CleverWrap("CC1cx7eaidCi0tvh7RfyC7eoYkA")
        clvrbot_msg_cnt = message.content.split(CLEVERBOT_COMMAND)[1]
        print ("Calling Cleverbot with " + clvrbot_msg_cnt + "...")
        answer = cw.say(clvrbot_msg_cnt)
        client.send_messagge(message.channel, answer)
        #"Hello Human."
        cw.reset() # resets the conversation ID and conversation state.
