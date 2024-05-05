# DiscordChanBot

Бот личного дискорд сервера

***
## todo
* [ ] Рейтиговая система
* [ ] Управление ролями по реакциям
* [ ] Создание дополнительных голосовых каналов и последующее их удаление
* [ ] Административные команды
* [*] Интеграция с БД

***
## Зависимости
* [discord.py](https://discordpy.readthedocs.io)


## Начало работы
Создать БД и пользователя для неё
CREATE DATABASE DiscordChanBot;
CREATE USER 'DiscordChanBot'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON DiscordChanBot.* TO 'DiscordChanBot'@'localhost';
FLUSH PRIVILEGES;