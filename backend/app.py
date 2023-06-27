from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware


from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService

import logging

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)

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
    json = {"Titulo": "Bienvenidos a la API - Vulnerable",
            "Cuatrimestre": "1 Cuatrimestre 2023",
            "Materia": "Criptografia y Seguridad Informática",
            "Autores": [
                {"Alumno": "Alejo Villores"},
                {"Alumno": "Ignacio Brusati"},
                {"Alumno": "Santiago Fernandez"},
                {"Alumno": "Ignacio Iragui"}
            ],
            "Version": "1.0.0",
            "Repositorio": "https://github.com/alejovillores/vulnerable-api-rest"

        }
    return json

@app.post("/register",status_code=201)
async def register(request: Request):
    try:
        logger = logging.getLogger('user_service')
        user_service = UserService(logger)
        json = await request.json()
        username = json["username"]
        password = json["password"]
        return user_service.register(db,username, password)
    except:
        raise HTTPException(status_code=400, detail="ya se encuentra ese usuario")

@app.post("/login",status_code=200)
async def login(request: Request, response: Response):
    try:
        logger = logging.getLogger('user_service')
        user_service = UserService(logger)
        json = await request.json()
        username = json["username"]
        password = json["password"]
        res = user_service.login(db,username, password)
        response.set_cookie(key="token", value=res, secure=False, samesite="none")
        return {"cookie": f"token={res}"}
    except:
        raise HTTPException(status_code=400, detail="error en login")


@app.get("/password/reset",status_code=200)
async def reset_password(request: Request, new_password: str):
    try:
        logger = logging.getLogger('user_service')
        token = request.cookies.get('token')
        if token != None:
            username, status = token.split('?')
            if bool(status):
                user_service = UserService(logger)
                res = user_service.reset_password(db,username,new_password)
                return res
        raise HTTPException(status_code=401, detail="No se encuentra la cookie")
    except:
        raise HTTPException(status_code=500, detail="Error en el reset de password")


@app.post("/password",status_code=201)
async def add_password(request: Request):
    try:
        logger = logging.getLogger('password_service')
        token = request.cookies.get('token')
        if token != None:
            username, status = token.split('?')
            if bool(status):
                password_service = PasswordService(logger)
                json = await request.json()
                app_username = json["app_username"]
                password = json["password"]
                app_name = json["app_name"]
                return password_service.add(db, username, app_username, password, app_name)
        raise HTTPException(status_code=401, detail="no se pudo encontrar la cookie")
    except e:
        raise e

@app.get("/password",status_code=200)
async def find_password(request: Request, app_name: str):
    try:
        logger = logging.getLogger('password_service')
        token = request.cookies.get('token')
        if token != None:
            username, status = token.split('?')
            if bool(status) :
                password_service = PasswordService(logger)
                return password_service.get(db,username,app_name)
    except:
        raise HTTPException(status_code=404, detail="no se pudo encontrar la contraseña")

@app.get("/passwords",status_code=200)
async def all_passwords(request: Request):
    try:
        logger = logging.getLogger('password_service')
        token = request.cookies.get('token')
        if token != None:
            username, status = token.split('?')
            if bool(status) :
                password_service = PasswordService(logger)
                return password_service.get_all(db,username)
    except:
        raise HTTPException(status_code=404, detail="no se pudo obtener las contraseñas")

