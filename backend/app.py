from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware


from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService
from auth.auth_handler import signJWT, decodeJWT

db = Database()
db.create_user_table()
db.create_password_table()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

def auth_user(request):
    try:
        token = request.cookies.get('token')
        return decodeJWT(token)
    except Exception as err:
        raise Exception(f"{err}")


@app.get("/")
async def root():
    json = {"Titulo": "Bienvenidos a la API - Segura",
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
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        return user_service.register(db,username, password)
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"ya se encuentra ese usuario {err}")

@app.post("/login",status_code=200)
async def login(request: Request, response: Response):
    try:
        user_service = UserService()
        json = await request.json()
        username = json["username"]
        password = json["password"]
        user_service.login(db,username, password)

        token = signJWT(username)
        response.set_cookie(key="token", value=token, samesite="Lax", httponly=True)
        return {"cookie": token}
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"error en login: {err}")


@app.get("/password/reset",status_code=200)
async def reset_password(request: Request, new_password: str):
    try:
        username = auth_user(request)
        user_service = UserService()
        res = user_service.reset_password(db, username, new_password)
        return res
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error en el reset de password {err}")

@app.post("/password",status_code=201)
async def add_password(request: Request):
    try:
        username = auth_user(request)
        password_service = PasswordService()
        json = await request.json()
        app_username = json["app_username"]
        password = json["password"]
        app_name = json["app_name"]
        return password_service.add(db, username, app_username, password, app_name)
    except Exception as err:
        raise HTTPException(status_code=401, detail=f"No se pudo insertar contraseña: {err}")

@app.get("/password",status_code=200)
async def find_password(request: Request, app_name: str):
    try:
        username = auth_user(request)
        password_service = PasswordService()
        return password_service.get(db,username,app_name)
    except Exception as err:
        raise HTTPException(status_code=404, detail=f"No se pudo encontrar la contraseña: {err}")

@app.get("/passwords",status_code=200)
async def all_passwords(request: Request):
    try:
        username = auth_user(request)
        password_service = PasswordService()
        return password_service.get_all(db,username)
    except Exception as err:
        raise HTTPException(status_code=404, detail=f"No se pudo obtener las contraseñas: {err}")

