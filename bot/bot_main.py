if __name__ == "__main__":
    print ("Please run main.py")
    exit()


import disnake
from disnake.ext import commands


from bot.bot_setting import settings_bot, settings_db
from database.db import *

#   Инициализируем бота
intents = disnake.Intents.default()                                                             # Подключаем "Разрешения"
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

command_flags = commands.CommandSyncFlags.default()
command_flags.sync_commands_debug = True

arkBot = commands.Bot(command_prefix=settings_bot['prefix'], intents=intents, command_sync_flags=command_flags )                       # Задаём префикс и интенты

base = database(settings_db['user'], settings_db['password'], settings_db['database'], settings_db['host'], settings_db['port'])
base.db_close()


import bot.usr_commands
import bot.adm_commands
import bot.events
# Функция запускающая бота и все его зависимости 
def botStart():
    

    arkBot.run(settings_bot['token'])
    pass    