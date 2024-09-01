from bot.bot_main import arkBot, base
from bot.phrases import phrases, command
import disnake, random



def handel_message(message):
    if message.author.bot:
        pass
    else:
        if base.db_user_read(message.author.id, message.guild.id) is None:
             base.db_user_create(message.author.global_name, message.author.name, message.author.id, message.guild.id )
        base.db_user_exp_add(message.author.id, random.randint(10, 30), message.guild.id)
    pass

# Реакция на загрузку бота
@arkBot.event
async def on_ready():
    print(f'Logged on as {arkBot.user} (ID: {arkBot.user.id})')                                 # Выводит имя подключенного бота и его ID
    print(f'Guilds:')
    base.db_connect()
    for guild in arkBot.guilds:
        print(f'{guild.name} : {guild.id}')
        base.db_table_create_init(guild.id)
        
        #if (base.db_table_check(guild.id) is None):
        #    base.db_table_create_init(guild.id)
        #    print('Таблица создана')
        #else:
        #    print('Таблица уже существует')
        
    base.db_close()


@arkBot.event
async def on_message(message):
    if message.author == arkBot.user:                                                       # не отвечать самому себе
                await arkBot.process_commands(message)
                return

    if 'донат' in message.content:                                                          # Случайное срабатывание на слово(для веселья)
        if round(random.gammavariate(1, 0.5)) == 1:
            embed = disnake.Embed(color= 0x87498f) 
            embed.set_image(url="https://tulen.store/storage/thumbs/1920x360_fit/LYCw088gGUthyWU0VoslL6W6iWi0rNLgL7Ldlf2A.jpg")
            embed.add_field(name = 'Лучший донат?', value =str(phrases['donate']), inline = False)   

            await message.channel.send(embed=embed)
    
    handel_message(message)
    

    await arkBot.process_commands(message)
    pass

@arkBot.event
async def on_guild_update(gbefore, gafter):
     print("Guild update")
     pass