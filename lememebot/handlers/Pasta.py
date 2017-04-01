import random
import re
import discord
import praw

''' TODO's:
get mentions of bot
Save pasatas
'''

class PastaBot():
    def __init__(self, client):
        self.client = client
        self.MIN_MSGS_BETWEEN_PASTA = 1
        self.MAX_MSGS_BETWEEN_PASTA = 3
        self.wait_between_msgs = random.randint(self.MIN_MSGS_BETWEEN_PASTA, self.MAX_MSGS_BETWEEN_PASTA)
        self.wait_between_msgs_count = 0
        self.reddit = praw.Reddit(client_id='x06_R0whglm1fA', client_secret="b7uHO17t4qm5Z6XjBGELZfTI3ng",
                     password='9zamir9', user_agent='testscript by /u/Vincible_',
                     username='Vincible_')

    async def on_message(self, client, message):
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
            elif self.WakeyWakeyTime():
                try:
                    # Get comments
                    comments = self.reddit.redditor('CummyBot2000').comments.top('month')    # You are my Queen, Cummy!  😍😍😍
                    comment = self.get_random_comment(comments)
                    copypasta = comment.body
                    
                    # Get rid of the evidence shhh bby
                    REEEEEEEEEEEE = re.compile(re.escape('cummybot'), re.IGNORECASE)
                    copypasta = REEEEEEEEEEEE.sub('leMemeBot69', copypasta)
                    await client.send_message(message.channel, copypasta)
                except Exception:
                    await client.send_message(message.channel, "something went wrong kiddo.")

    def SetSettings(self, command, num):
        commands = ['setmin', 'setmax', 'stop', 'resume']
        ayyMsgs =   {(0):["Do you want infinite pastas? \n Because that's how you get infinite pastas. Have fun."],
                    (1,7):["FUCK YEAH!","My man!", "Oh yeah baby", "😘😘😘", "ヽ(^◇^*)/"],
                    (8,15):["Really? fine...","Wow that\s a great way to ruin fun!", "...","P-Pls Senapi don't do this  (｡✿‿✿｡)"],
                    (16,100):["You suck.", "Fuck off", "You should kill yourself for what you just did, just sayin'"],
                    (100): ["Ore wa ochinchin ga daisuki nandayo"]}

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
        if num < 0:
            self.MIN_MSGS_BETWEEN_PASTA = 0
            self.MAX_MSGS_BETWEEN_PASTA = 1
            return ayyMsgs.get((1))
        elif num >= 100:
            return ayyMsgs.get((100))
        else:
            for key in ayyMsgs:
                if type(key).__name__ == 'tuple' and key[0] <= num <= key[1]:
                    return random.choice(ayyMsgs.get(key))

    def WakeyWakeyTime(self):
        self.wait_between_msgs_count += 1
        print(self.wait_between_msgs_count)
        print(self.wait_between_msgs)
        print(self.MIN_MSGS_BETWEEN_PASTA)
        print(self.MAX_MSGS_BETWEEN_PASTA)
        if self.wait_between_msgs_count >= self.wait_between_msgs:
            self.wait_between_msgs = random.randint(self.MIN_MSGS_BETWEEN_PASTA, self.MAX_MSGS_BETWEEN_PASTA)
            self.wait_between_msgs_count = 0
            return True # oh yeahhh lets go BABBBYYYY
        else:
            return False

    def get_random_comment(self, comments):
        num = random.randint(0,99)
        count = 0
        # Why isn't this Index Based ¯\_(ツ)_/¯
        for comment in comments:
            if (count == num):
                return comment
            count += 1