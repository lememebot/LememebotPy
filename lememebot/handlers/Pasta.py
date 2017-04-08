import random
import re
import discord
import praw

''' TODO's:
Set typing when cooking
Search pastas
Save video/audio to commands (e.g !setvoice yeahboi youtubeYeahboiURL afterwhich !yeahboi would play the URL)
'''

class PastaBot():
    def __init__(self, client):
        self.client = client
        self.MIN_MSGS_BETWEEN_PASTA = 1
        self.MAX_MSGS_BETWEEN_PASTA = 3
        self.wait_between_msgs = random.randint(self.MIN_MSGS_BETWEEN_PASTA, self.MAX_MSGS_BETWEEN_PASTA)
        self.wait_between_msgs_count = 0
        self.reddit = praw.Reddit(client_id='x06_R0whglm1fA',
                                  client_secret="b7uHO17t4qm5Z6XjBGELZfTI3ng",
                                  password='',
                                  user_agent='testscript by /u/Vincible_',
                                  username='')

    async def on_message(self, client, message):

        print('[DEBUG: PastaBot] in on_message')

        if message.author.id != client.user.id:
            # Copying stuff from Yoni thnx bby 😘
            args = str.lower(message.content).split(sep=' ')
            if args[0] == '!pasta':
                try:
                    response = self.SetSettings(args[1], int(args[2]))
                    self.wait_between_msgs = random.randint(self.MIN_MSGS_BETWEEN_PASTA, self.MAX_MSGS_BETWEEN_PASTA)
                    await client.send_message(message.channel, response)
                except Exception:
                    await client.send_message(message.channel, "something went wrong kiddo.")
            # Check if it's wakeywakey time
            elif (client.user.mentioned_in(message)
                  or self.WakeyWakeyTime() or
                  "pasta" in message.content):
                await client.send_message(message.channel, self.GeneratePasta())

    def SetSettings(self, command, num):
        commands = ['setmin', 'setmax', 'stop', 'resume']
        ayyMsgs =   {(0): "Do you want infinite pastas? \nBecause that's how you get infinite pastas. Have fun.",
                    (1,7):["FUCK YEAH!","My man!", "Oh yeah baby", "😘😘😘", "ヽ(^◇^*)/"],
                    (8,15):["Really? fine...","Wow that's a great way to ruin fun!", "...","P-Pls Senapi don't do this  (｡✿‿✿｡)"],
                    (16,100):["You suck.", "Fuck off", "You should kill yourself for what you just did, just sayin'"],
                    (100): "Ore wa ochinchin ga daisuki nandayo"}

        isMin = False    # meirl
        if command not in commands:
            return "Unknown command"
        elif ((command == 'setmin' and num > self.MAX_MSGS_BETWEEN_PASTA) or
            (command == 'setmax' and num < self.MIN_MSGS_BETWEEN_PASTA)):
            return "setmin value must be lower than setmax value."
        elif command == 'setmin':
            self.MIN_MSGS_BETWEEN_PASTA = num
        elif command == 'setmax':
            self.MAX_MSGS_BETWEEN_PASTA = num

        # Generate response
        if num <= 0:
            self.MIN_MSGS_BETWEEN_PASTA = 0
            self.MAX_MSGS_BETWEEN_PASTA = 1
            return ayyMsgs.get((0))
        elif num >= 100:
            return ayyMsgs.get((100))
        else:
            for key in ayyMsgs:
                if type(key).__name__ == 'tuple' and key[0] <= num <= key[1]:
                    return random.choice(ayyMsgs.get(key))

    def GeneratePasta(self):
        try:
            # Reset the counters
            self.wait_between_msgs = random.randint(self.MIN_MSGS_BETWEEN_PASTA, self.MAX_MSGS_BETWEEN_PASTA)
            self.wait_between_msgs_count = 0

            # Get random post
            comments = self.reddit.redditor('CummyBot2000').comments.top('month')    # You are my Queen, Cummy!  😍😍😍
            comment = self.get_random_comment(comments)
            copypasta = comment.body

            # Get rid of the evidence shhh bby
            REEEEEEEEEEEE = re.compile(re.escape('cummybot'), re.IGNORECASE)
            copypasta = REEEEEEEEEEEE.sub('leMemeBot69', copypasta)
        except Exception:
            copypasta = "something went wrong kiddo."
        return copypasta
    def WakeyWakeyTime(self):
        self.wait_between_msgs_count += 1

        # oh yeahhh lets go BABBBYYYY
        return self.wait_between_msgs_count >= self.wait_between_msgs

    def get_random_comment(self, comments):
        num = random.randint(0,99)
        count = 0
        # Why isn't this Index Based ¯\_(ツ)_/¯
        for comment in comments:
            if (count == num):
                return comment
            count += 1
