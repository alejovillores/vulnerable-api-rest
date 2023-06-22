class PasswordService: 

    def add(self,db,username,app_username, password,app_name):
        sql_sentence = "SELECT * FROM users WHERE username = ?"

        res = db.put(sql_sentence, (username,))
        if res.fetchone() != None:
            sql_sentence = "INSERT INTO passwords VALUES(?,?,?,?);"
            db.put(sql_sentence,(username, app_username, password, app_name))
            return {"username": app_username, "password_status": "OK", "dst": app_name} 
        raise Exception('exception')

    def get(self,db,username,app_name):
        sql_sentence = "SELECT * FROM passwords WHERE app_name LIKE ? AND username = ? "
        res = db.put(sql_sentence, (app_name, username))

        data = res.fetchall()
        for i in range(len(data)):
            json = {
                "username":data[i][0],
                "app_username":data[i][1],
                "password":data[i][2],
                "app_name":data[i][3],
            }
            data[i] = json

        return data

    def get_all(self,db,username):
        sql_sentence = "SELECT * FROM passwords WHERE username = ?"
        res = db.put(sql_sentence, (username,))
        data = res.fetchall()
        for i in range(len(data)):
            json = {
                "username":data[i][0],
                "app_username":data[i][1],
                "password":data[i][2],
                "app_name":data[i][3],
            }
            data[i] = json

        return data