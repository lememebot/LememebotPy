import webbrowser
import asyncio

class RunGameBeta:
    RUN_GAME_CMD = "!run"
    SET_GAME_CMD = "!set"

    def __init__(self):
        self.apps_dict = dict()

    # will tell dean to shut the fuck up when he goes nuts
    async def on_message(self, client, message):
        print('[DEBUG: RunGameBeta] in on_message')
        if message.content.startswith(self.SET_GAME_CMD):
            game_cmd_params = message.content.split(self.SET_GAME_CMD + " ")[1].split(" ")
            self.apps_dict[game_cmd_params[0]] = game_cmd_params[1]

            await client.send_message(destination=message.channel, content='Added app {0} with id {1}'.format(game_cmd_params[0], game_cmd_params[1]))

        elif message.content.startswith(self.RUN_GAME_CMD):
            game_name = message.content.split(self.RUN_GAME_CMD + " ")[1]
            await client.send_message(destination=message.channel, content='Running {0}...'.format(game_name))
            webbrowser.open("steam://run/{0}".format(self.apps_dict[game_name]), new=0 ,autoraise=True)
