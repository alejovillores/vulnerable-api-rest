from fastapi import FastAPI, Request, HTTPException, Response
from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService



db = Database()
db.create_user_table()
db.create_password_table()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register",status_code=201)
async def register(request: Request):
    try:
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        return user_service.register(db,username, password)
    except:
        raise HTTPException(status_code=400, detail="error")


@app.post("/login",status_code=200)
async def login(request: Request, response: Response):
    try:
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        res = user_service.login(db,username, password)
        response.set_cookie(key="auth", value=str(res))
        return res
    except:
        raise HTTPException(status_code=401, detail="login invalido")


@app.post("/password",status_code=201)
async def add_password(request: Request):
    try:
        cookie = request.cookies.get('auth')
        if bool(cookie):
            password_service = PasswordService()
            json = await request.json()
            username = json["username"]
            password = json["password"]
            dst = json["dst"]
            return password_service.add(db,username,password,dst)
    except:
        raise HTTPException(status_code=401, detail="no se pudo insertar contraseña")
