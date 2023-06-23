import jwt
import os
from dotenv import load_dotenv
import time

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
TOKEN_TTL = float(os.getenv('TOKEN_TTL'))


def signJWT(username):
    payload = {
        "username": username,
        "expires": time.time() + TOKEN_TTL
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token['username']
        raise Exception('Expired token')
    except:
        raise Exception('Invalid token')