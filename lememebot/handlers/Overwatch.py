# will tell dean to shut the fuck up when he goes nuts
def on_cmd_hello(client,message,param):
    print(param)
    client.send_message(destination=message.channel,content='Playing ' + param)

def get_command_delegate(cmd):
    return cmd_delegates.get(cmd)

cmd_delegates = { 'hello' : on_cmd_hello }


