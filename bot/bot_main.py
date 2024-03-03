import discord
from discord.ext import commands

from bot.bot_setting import *

#   Инициализируем бота
intents = discord.Intents.default()                                             # Подключаем "Разрешения"
intents.message_content = True

arkBot = commands.Bot(command_prefix='?', intents=intents)                      # Задаём префикс и интенты

# С помощью декоратора создаём первую команду
@arkBot.command()
async def ping(message):
    await message.send('pong')


@arkBot.event
async def on_ready():
        print(f'Logged on as {arkBot.user}, (ID: {arkBot.user.id})')


@arkBot.event
async def on_message(message):
        # don't respond to ourselves
        if message.author == arkBot.user:
            return
        if 'ping' in message.content:
            await message.channel.send('pong')








#малозначащая функция на текущий момент
def botStart():
    arkBot.run(settings['token'])
    pass    