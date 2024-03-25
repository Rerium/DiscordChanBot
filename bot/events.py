from bot.bot_main import arkBot
from bot.phrases import phrases, command

# Реакция на загрузку бота
@arkBot.event
async def on_ready():
    print(f'Logged on as {arkBot.user} (ID: {arkBot.user.id})')                                 # Выводит имя подключенного бота и его ID

