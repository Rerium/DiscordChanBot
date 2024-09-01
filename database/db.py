import mysql.connector as mariadb
from mysql.connector import Error

        
class database:
    db_user = ''
    db_pass = ''
    db_name = ''
    db_host = ''
    db_port = ''
    db_connection = object()
    
    def __init__ (self, user:str, password:str, name:str, host:str, port:int):
        try:
            self.db_user = user
            self.db_pass = password
            self.db_name = name
            self.db_host = host
            self.db_port = port
            db_connection_t = mariadb.connect (user = self.db_user, password = self.db_pass, database = self.db_name, host = self.db_host, port = self.db_port )
            self.db_connection = db_connection_t
            print('Подключение к базе данных выполнено успешно')
            
        except Error as error:
            print(f'Ошибка подключения к БД: {error}')
            
        pass

    def db_close(self):
        self.db_connection.close()
        #print('Подключение к базе данных закрыто')
        pass

    def db_connect(self):
        try:
            self.db_connection = mariadb.connect (user = self.db_user, password = self.db_pass, database = self.db_name, host = self.db_host, port = self.db_port )
            #print('Подключение к базе данных выполнено успешно', self.db_connection)
        except Error as error:
            print(f'Ошибка подключения к БД: {error}')

        pass
    
    def db_user_read(self, user_id:int, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM `users_"+ str(guild) +"` WHERE user_id = " + str(user_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        self.db_close()
        return result
        
    def db_user_exp_add(self, user_id:int, exp:int, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "UPDATE `users_"+ str(guild) +"` SET exp = exp + " + str(exp) + " WHERE user_id = `" + str(user_id) +"`" 
        cursor.execute(sql)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_upd_nickname(self, user_id:int, nickname:str, guild):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "UPDATE `users_"+ str(guild) +"` SET global_name = "+ nickname + " WHERE user_id = " + str(user_id)
        cursor.execute(sql)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_upd_username(self, user_id:int, username:str, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "UPDATE `users_"+ str(guild) +"` SET username = " + username +" WHERE user_id = " + str(user_id)
        cursor.execute(sql)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_create(self, nickname:str, username:str, user_id:int, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO `users_"+ str(guild) +"` (global_name, username, user_id) VALUES (%s, %s, %s)"
        values = (nickname, username, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_admin_create(self, user_id:int, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO `admins_"+ str(guild) +"` (user_id) VALUES (%s)"
        values = (user_id,)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_admin_search(self, user_id:int, guild:int) -> tuple:
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM `admins_"+ str(guild) +"` WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.db_close()
        return result

    def db_admin_del(self, user_id:int, guild:int):
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM `admins_"+ str(guild) +"` WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_close(self):
        self.db_connection.close()
        pass



    def db_user_search(self, user_id:int, guild:int) -> tuple:
        self.db_connect()
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM `users_"+ str(guild) +"` WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.db_close()
        return result
    
    def db_table_check(self, guild:int):
        cursor = self.db_connection.cursor()
        sql = "SHOW TABLES LIKE `users_"+ str(guild) +"` FROM "+ self.db_name
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def db_table_create_init(self, guild: int) -> object:
        cursor = self.db_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS `DiscordChanBot`.`users_"+ str(guild) +"`  (`user_id` BIGINT NOT NULL , `username` VARCHAR(32) NOT NULL , `global_name` VARCHAR(32) NOT NULL , `exp` INT NOT NULL DEFAULT '0' ) ENGINE = InnoDB; "
        cursor.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS `DiscordChanBot`.`admins_"+ str(guild) +"` (`user_id` BIGINT NOT NULL) ENGINE = InnoDB; "
        cursor.execute(sql)
        self.db_connection.commit()
        pass

