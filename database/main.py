import mysql.connector as mariadb
from mysql.connector import Error


        
class database:
    db_user = ''
    db_pass = ''
    db_name = ''
    db_host = ''
    db_port = ''
    db_connection = None
    
    
    def __init__ (self, user, password, name, host, port):
        try:
            self.db_user = user
            self.db_pass = password
            self.db_name = name
            self.db_host = host
            self.db_port = port
            self.db_connection = mariadb.connect (user = self.db_user, password = self.db_pass, database = self.db_name, host = self.db_host, port = self.db_port )
            print('Подключение к базе данных выполнено успешно', self.db_connection)
            
        except Error as error:
            print(f'Ошибка подключения к БД: {error}')
            
        pass
    
    def db_close(self):
        self.db_connection.close()
        print('Подключение к базе данных закрыто')
        pass
    
    def db_read_user(self, user_id):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM users WHERE id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
        
    def db_user_exp_add(self, user_id, exp):
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET exp = exp + %s WHERE id = %s"
        values = (exp, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        pass

    def db_user_upd_nickname(self, user_id, nickname):
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET nickname = %s WHERE id = %s"
        values = (nickname, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        pass

    def db_user_upd_username(self, user_id, username):
        cursor = self.db_connection.cursor()
        sql = "UPDATE users SET username = %s WHERE id = %s"
        values = (username, user_id)
        cursor.execute(sql, values)
        self.db_connection.commit()
        pass

