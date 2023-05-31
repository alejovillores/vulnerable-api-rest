from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware

from cryptography.fernet import Fernet

from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService



# Generate a Fernet key
key = Fernet.generate_key()

# Create a Fernet object with that key
f = Fernet(key)

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
        raise HTTPException(status_code=400, detail="error")


@app.post("/login",status_code=200)
async def login(request: Request):
    try:
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        res = user_service.login(db,username, password)
        encrypted_string = f.encrypt(res.encode())
        return {"token": encrypted_string}
    except:
        raise HTTPException(status_code=400, detail="login invalido")


@app.post("/password",status_code=201)
async def add_password(request: Request, token: str):
    try:
        decrypted_text = f.decrypt(token)
        data = decrypted_text.decode()
        username, status = data.split('?')
        if bool(status):
            print("pasa")
            password_service = PasswordService()
            json = await request.json()
            app_username = json["app_username"]
            password = json["password"]
            app_name = json["app_name"]
            return password_service.add(db, username, app_username, password, app_name)
    except:
        raise HTTPException(status_code=401, detail="no se pudo insertar contraseña")

@app.get("/password",status_code=200)
async def find_password(request: Request, app_name: str, token: str):
    decrypted_text = f.decrypt(token)
    data = decrypted_text.decode()
    username, status = data.split('?')
    if bool(status) :
        password_service = PasswordService()
        return password_service.get(db,username,app_name)
