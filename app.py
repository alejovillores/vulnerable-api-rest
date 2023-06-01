from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware


from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService

db = Database()
db.create_user_table()
db.create_password_table()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        raise HTTPException(status_code=400, detail="ya se encuentra ese usuario")

@app.post("/login",status_code=200)
async def login(request: Request, response: Response):
    try:
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        res = user_service.login(db,username, password)
        response.set_cookie(key="token", value=res)
        return {"cookie": res}
    except:
        raise HTTPException(status_code=400, detail="error en login")


@app.post("/password",status_code=201)
async def add_password(request: Request):
    try:
        token = request.cookies.get('token')
        if token != None:
            username, status = token.split('?')
            if bool(status):
                password_service = PasswordService()
                json = await request.json()
                app_username = json["app_username"]
                password = json["password"]
                app_name = json["app_name"]
                return password_service.add(db, username, app_username, password, app_name)
        raise HTTPException(status_code=401, detail="no se pudo encontrar la cookie")
    except:
        raise HTTPException(status_code=401, detail="no se pudo insertar contraseña")

@app.get("/password",status_code=200)
async def find_password(request: Request, app_name: str):
    
    token = request.cookies.get('token')
    if token != None:
        username, status = token.split('?')
        if bool(status) :
            password_service = PasswordService()
            return password_service.get(db,username,app_name)


