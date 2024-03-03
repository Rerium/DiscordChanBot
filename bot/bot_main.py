import discord
from bot.bot_setting import *

class arkBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


def botStart():
    intents = discord.Intents.default()
    intents.message_content = True
    client = arkBot(intents=intents)
    client.run(settings['token'])
    pass    