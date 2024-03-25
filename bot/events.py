from bot.bot_main import arkBot
from bot.phrases import phrases, command
import disnake, random

# Реакция на загрузку бота
@arkBot.event
async def on_ready():
    print(f'Logged on as {arkBot.user} (ID: {arkBot.user.id})')                                 # Выводит имя подключенного бота и его ID

@arkBot.event
async def on_message(message):
    if message.author == arkBot.user:                                                       # не отвечать самому себе
                await arkBot.process_commands(message)
                return

    if 'донат' in message.content:                                                          # Рандомное срабатывание на слово(для веселья)
        if (round(random.gammavariate(1, 0.5)) == 1):
            embed = disnake.Embed(color= 0x87498f) 
            embed.set_image(url="https://tulen.store/storage/thumbs/1920x360_fit/LYCw088gGUthyWU0VoslL6W6iWi0rNLgL7Ldlf2A.jpg")
            embed.add_field(name = 'Лучший донат?', value =str(phrases['donate']), inline = False)   

            await message.channel.send(embed=embed)
            
    await arkBot.process_commands(message)
    pass