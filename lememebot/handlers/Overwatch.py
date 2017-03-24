import discord

commands = [('hello',on_cmd_hello)]

#!hello yoni suyck s => param = yoni siucks oytmnskrj
# will tell dean to shut the fuck up when he goes nuts
def on_message(message):
    print('Hey')

def on_cmd_hello(client,param):
