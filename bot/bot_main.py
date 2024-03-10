import discord
from discord.ext import commands
import random

from bot.bot_setting import *
from bot.phrases import phrases, command

#   Инициализируем бота
intents = discord.Intents.default()                                                             # Подключаем "Разрешения"
intents.message_content = True

arkBot = commands.Bot(command_prefix=settings['prefix'], intents=intents)                       # Задаём префикс и интенты

# Ping
@arkBot.command()
async def ping(message):
    await message.send("pong")
    pass

# Список команд
@arkBot.command()
async def list(message):
    msg = ""
    for cmd in command:
        msg = msg + cmd+'\n'
    await message.send(str(msg))
    pass

# Информация о боте     
@arkBot.command()
async def info(message):
    file = discord.File("bot/image/info.png", filename="info.png")

    embed = discord.Embed(color= 0x87498f) 
    embed.set_image(url="attachment://info.png")
    embed.add_field(name = 'Информация о боте', value =str(phrases['info']), inline = False)   

    await message.send(file=file, embed=embed)
    pass

# Бросает кость
@arkBot.command()
async def dice(message):
    await message.send(str(random.randrange(6)+1))

# Реакция на загрузку бота
@arkBot.event
async def on_ready():
    print(f'Logged on as {arkBot.user} (ID: {arkBot.user.id})')                                 # Выводит имя подключенного бота и его ID




# Функция запускающая бота и все его зависимости 
def botStart():
    random.seed()

    arkBot.run(settings['token'])
    pass    