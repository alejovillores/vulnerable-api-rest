class PasswordService: 

    def add(self,db,username,password,dst):
        sql_sentence = "SELECT * FROM users WHERE username = '{}'".format(username)
        res = db.execute(sql_sentence)
        if res.fetchone() != None:
            sql_sentence = "INSERT INTO passwords VALUES(?,?,?);"
            db.put(sql_sentence,(username,password,dst))
            return {"username": username, "password_status": "OK", "dst": dst} 
        raise Exception('exception')