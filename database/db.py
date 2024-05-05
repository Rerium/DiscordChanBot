from queue import Full
import mysql.connector as mariadb
from mysql.connector import Error

        
class database:
    db_user = ''
    db_pass = ''
    db_name = ''
    db_host = ''
    db_port = ''
    db_connection = object()
    
    def __init__ (self, user, password, name, host, port):
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

    def db_conntion(self):
        try:
            self.db_connection = mariadb.connect (user = self.db_user, password = self.db_pass, database = self.db_name, host = self.db_host, port = self.db_port )
            #print('Подключение к базе данных выполнено успешно', self.db_connection)
        except Error as error:
            print(f'Ошибка подключения к БД: {error}')

        pass
    
    def db_read_user(self, user_id):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM users WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.db_close()
        return result
        
    def db_user_exp_add(self, user_id, exp):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET exp = exp + %s WHERE user_id = %s"
        values = (exp, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_upd_nickname(self, user_id, nickname):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET global_name = %s WHERE user_id = %s"
        values = (nickname, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_upd_username(self, user_id, username):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET username = %s WHERE user_id = %s"
        values = (username, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_create(self, nickname, username, user_id):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO users (global_name, username, user_id) VALUES (%s, %s, %s)"
        values = (nickname, username, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        self.db_close()
        pass

    def db_user_search(self, user_id):
        self.db_conntion()
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM users WHERE user_id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.db_close()
        return result
    
    def db_table_check(self):
        cursor = self.db_connection.cursor()
        sql = "SHOW TABLES FROM "+ self.db_name
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def db_table_create_init(self):
        cursor = self.db_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS `DiscordChanBot`.`users` (`user_id` BIGINT NOT NULL , `username` VARCHAR(32) NOT NULL , `global_name` VARCHAR(32) NOT NULL , `exp` INT NOT NULL DEFAULT '0' ) ENGINE = InnoDB; "
        cursor.execute(sql)
        self.db_connection.commit()
        pass

