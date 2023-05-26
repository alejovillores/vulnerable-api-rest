from fastapi import FastAPI, Request,HTTPException
from db.config import Database
from services.user_service import UserService


db = Database()
db.create_user_table()
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
async def login(request: Request):
    user_service = UserService()
    json = await request.json()
    username = json["username"]
    password = json["password"]

    return user_service.login(db,username, password)
