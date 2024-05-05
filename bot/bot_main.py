if __name__ == "__main__": 
    print ("Please run main.py")
    exit()


import disnake
from disnake.ext import commands


from bot.bot_setting import settings, db
from database.db import *

#   Инициализируем бота
intents = disnake.Intents.default()                                                             # Подключаем "Разрешения"
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

arkBot = commands.Bot(command_prefix=settings['prefix'], intents=intents, sync_commands_debug=False)                       # Задаём префикс и интенты

base = database(db['user'], db['password'], db['database'], db['host'], db['port'])
if (base.db_table_check() == None):
    base.db_table_create_init()
    print('Таблица создана')
else:
    print('Таблица уже существует')
    
base.db_close()


import bot.commands
import bot.events
# Функция запускающая бота и все его зависимости 
def botStart():
    

    arkBot.run(settings['token'])
    pass    