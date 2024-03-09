import discord
from discord.ext import commands
import random, os

from bot.bot_setting import *
from bot.phrases import phrases, triggers, command

#   Инициализируем бота
intents = discord.Intents.default()                                                             # Подключаем "Разрешения"
intents.message_content = True

arkBot = commands.Bot(command_prefix=settings['prefix'], intents=intents)                       # Задаём префикс и интенты

# С помощью декоратора создаём первую команду
@arkBot.command()
async def ping(message):
    await message.send("pong")
    pass

@arkBot.command()
async def list(message):
    msg = ""
    for cmd in command:
        msg = msg + cmd+'\n'
    await message.send(str(msg))
    pass
        
@arkBot.command()
async def info(message):
    file = discord.File("bot/image/info.png", filename="info.png")

    embed = discord.Embed(color= 0x87498f) 
    embed.set_image(url="attachment://info.png")
    embed.add_field(name = 'Информация о боте', value =str(phrases['info']), inline = False)   

    await message.send(file=file, embed=embed)
    pass


                



@arkBot.event
async def on_ready():
    print(f'Logged on as {arkBot.user}, (ID: {arkBot.user.id})')

@arkBot.event
async def on_guild_join(test):
    await print(test)
     

""" @arkBot.event
async def on_message(message):
    if message.author == arkBot.user:                                                       # не отвечать самому себе
        return
        
    if 'донат' in message.content:                                                          # Рандомное срабатывание на слово(для веселья)
        if (round(random.gammavariate(1, 0.5)) == 1):
            await message.channel.send(phrases['donate']) """

#малозначащая функция на текущий момент
def botStart():
    random.seed()

    arkBot.run(settings['token'])
    pass    