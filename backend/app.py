from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


from db.config import Database
from services.user_service import UserService
from services.password_service import PasswordService
from auth.auth_handler import signJWT, decodeJWT
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

app = FastAPI()

WILDCARD = "*"

class DomainFilterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: RequestResponseEndpoint, allowed_domains: list[str], allow_methods: list[str]):
        super().__init__(app)
        self.allowed_domains = allowed_domains
        self.allowed_methods = allowed_methods

    def allowed_client(self, address, port):
        for domain in self.allowed_domains:
            if domain != WILDCARD and address != domain[0]:
                continue
            if domain[1] == WILDCARD or domain[1] == port:
                return True
        return False
    
    def allowed_method(self, method):
        all_allowed = WILDCARD in self.allowed_methods
        method_allowed = method in self.allowed_methods

        return all_allowed or method_allowed

    async def dispatch(self, request: Request, call_next):
        print(vars(request))

        address = request.client[0]
        port = request.client[1]
        if not self.allowed_client(address, port):
            return Response(content="Domain Not Authorized", status_code=401)
        
        method = request.method
        if not self.allowed_method(method):
            return Response(content="Method Not Authorized", status_code=401)

        return await call_next(request)


db = Database()
db.create_user_table()
db.create_password_table()


app = FastAPI()

allowed_domains = [("127.0.0.1", 4200), ('127.0.0.1', "*")]
allowed_methods = ["GET", "POST", "OPTIONS"]
# app.add_middleware(DomainFilterMiddleware, allowed_domains=allowed_domains, allowed_methods=allowed_methods)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
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
        raise HTTPException(status_code=400, detail=f"Error en register {err}")

@app.post("/login", status_code=200)
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
        raise HTTPException(status_code=400, detail=f"Error en login: {err}")


@app.post("/password/reset", status_code=200)
async def reset_password(request: Request):
    try:
        username = auth_user(request)
        json = await request.json()
        new_password = json["new_password"]
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