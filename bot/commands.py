import disnake, random
from bot.bot_main import arkBot
from bot.phrases import phrases, command
random.seed()

# Ping
@arkBot.slash_command(  name="ping",
                        description="Возращает задержку бота",
                     )
async def ping(message: disnake.ApplicationCommandInteraction):
    await message.send("pong")
    pass

# Список команд
# @arkBot.slash_command(  name="list",
#                         description="Отображает все команды",
#                      )
# async def list(message: disnake.ApplicationCommandInteraction):    
#     msg = ""
#     for cmd in command:
#         msg = msg + cmd+'\n'
#     await message.send(str(msg))
#     pass

# Информация о боте     
@arkBot.slash_command(  name="info",
                        description="Информация о боте",
                     )
async def info(message: disnake.ApplicationCommandInteraction):
    file = disnake.File("bot/image/info.png", filename="info.png")

    embed = disnake.Embed(color= 0x87498f) 
    embed.set_image(url="attachment://info.png")
    embed.add_field(name = 'Информация о боте', value =str(phrases['info']), inline = False)   

    await message.send(file=file, embed=embed)
    pass

# Бросает кость
@arkBot.slash_command(  name="dice",
                        description="Бросает кость d6",
                     )
async def dice(message):
    await message.send(str(random.randrange(6)+1))

# информация о сервере
@arkBot.slash_command(description="Информация о сервере")
async def server(message):
    await message.response.send_message(
        f"Название сервера: {message.guild.name}\nВсего участников: {message.guild.member_count}"
    )
