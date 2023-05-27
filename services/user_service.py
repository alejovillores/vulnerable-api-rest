import hashlib
class UserService: 
    def __init__(self):
        self.hasher = hashlib.md5()


    def register(self,db,username, password):
        sql_sentence = "SELECT * FROM users WHERE username = '{}'".format(username)
        res = db.execute(sql_sentence)
        print("res:", res)
        if res.fetchone() == None:
            self.hasher.update(password.encode())
            hashed = self.hasher.hexdigest()    
            print ("HASHED:" + hashed)
            sql_sentence = "INSERT INTO users VALUES(?,?);"
            print(sql_sentence)
            db.put(sql_sentence,(username,hashed))
            
            return {"username": username, "password": hashed} 
        raise Exception('exception')
        


    def login(self,db, username, password): 
        self.hasher.update(password.encode())
        hashed = self.hasher.hexdigest()
        
        sql_sentence = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username,hashed) 
        res = db.execute(sql_sentence)
    
        if res.fetchone() is not None:
            return True
        
        raise Exception('invalid')