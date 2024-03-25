import disnake
from disnake.ext import commands


from bot.bot_setting import *


#   Инициализируем бота
intents = disnake.Intents.default()                                                             # Подключаем "Разрешения"
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

arkBot = commands.Bot(command_prefix=settings['prefix'], intents=intents, sync_commands_debug=True)                       # Задаём префикс и интенты

import bot.commands
import bot.events

# Функция запускающая бота и все его зависимости 
def botStart():
    

    arkBot.run(settings['token'])
    pass    