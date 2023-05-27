class PasswordService: 

    def add(self,db,username,password,app_name):
        sql_sentence = "SELECT * FROM users WHERE username = '{}'".format(username)
        res = db.execute(sql_sentence)
        if res.fetchone() != None:
            sql_sentence = "INSERT INTO passwords VALUES(?,?,?);"
            db.put(sql_sentence,(username,password,dst))
            return {"username": username, "password_status": "OK", "dst": app_name} 
        raise Exception('exception')

    def get(self,db,username,app_name):
        sql_sentence = "SELECT * FROM passwords WHERE appName = '{}' AND username = '{}' ".format(app_name,username) 
        print(sql_sentence)
        res = db.execute(sql_sentence)
        return res.fetchall()
