import hashlib
class UserService: 
    def __init__(self):
        self.hasher = hashlib.md5()


    def register(self,db,username, password):
        sql_sentence = "SELECT * FROM users WHERE username = ?"
        res = db.put(sql_sentence, (username,))
        if res.fetchone() == None:
            self.hasher.update(password.encode())
            hashed = self.hasher.hexdigest()    
            sql_sentence = "INSERT INTO users VALUES(?,?);"
            db.put(sql_sentence,(username,hashed))
            
            return {"username": username, "password": hashed} 
        raise Exception('exception')
        


    def login(self, db, username, password): 
        self.hasher.update(password.encode())
        hashed = self.hasher.hexdigest()
        
        sql_sentence = "SELECT * FROM users WHERE username = ? AND password = ?"
        res = db.put(sql_sentence, (username,hashed))
    
        if res.fetchone() is not None:
            token = '{}?{}'.format(username,True)
            return token
    
        raise Exception('invalid')
    
    def reset_password(self,db,username,new_password):
        sql_sentence = "SELECT * FROM users WHERE username = ?"
        res = db.put(sql_sentence, (username,))
        if res.fetchone() != None:
            self.hasher.update(new_password.encode())
            hashed = self.hasher.hexdigest()    
            sql_sentence = "UPDATE users SET password = ? WHERE username = ?"
            db.put(sql_sentence, (hashed,username))
            return {"username": username, "new_password": hashed} 
        raise Exception('exception')
