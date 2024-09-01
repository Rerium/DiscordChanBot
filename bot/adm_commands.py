import disnake
from bot.bot_main import arkBot, base

@arkBot.slash_command(  name="admin_add",
                        description="Добавление администратора",
                     )
async def admin_add(message: disnake.ApplicationCommandInteraction, user: disnake.User):
    if message.author.id == message.guild.owner.id:
        base.db_admin_create(user.id, message.guild.id)
        await message.response.send_message(f"<@{user.id}> добавлен как администратор")
    else:
        await message.response.send_message("Вы не админ")
    pass

@arkBot.slash_command(  name="admin_del",
                      description="Удаляет админа",
                    )
async def admin_del(message: disnake.ApplicationCommandInteraction, user: disnake.User):
    if message.author.id == message.guild.owner.id:
        base.db_admin_del(user.id, message.guild.id)
        await message.response.send_message(f"<@{user.id}> удален как администратор")
    else:
        await message.response.send_message("Вы не админ")
    pass

# информация о сервере
@arkBot.slash_command(description="Информация о сервере")
async def server(message):
    if message.author.id == message.guild.owner.id:
        await message.response.send_message(
            f"Название сервера: {message.guild.name}\nВсего участников: {message.guild.member_count}"
        )
    else:
        await message.response.send_message("Вы не админ")
    pass

def adm_check(admin_id, guild):
    adm = base.db_admin_search( admin_id, guild)



