import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("api-seguridad.db")

    def create_user_table(self):
        sql_sentence = "create table if not exists users(username TEXT, password TEXT)"
        cursor = self.con.cursor()
        cursor.execute(sql_sentence)
    
    def create_password_table(self):
        sql_sentence = "create table if not exists passwords(username TEXT, app_username TEXT, password TEXT, app_name TEXT)"
        cursor = self.con.cursor()
        cursor.execute(sql_sentence)

    def execute(self, sql_sentence):
        cursor = self.con.cursor()
        res = cursor.execute(sql_sentence)
        return res
    
    def put(self, sql_sentence,data):
        cursor = self.con.cursor()
        res = cursor.execute(sql_sentence,data)
        self.con.commit()
        return res
    

    def close(self):
        self.connection.close()



         