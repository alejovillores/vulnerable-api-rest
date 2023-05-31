# VULNERABLE API

Start server

`python3 ./main.py`


## Endpoints

#### POST users

```POST /login HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 52

{
    "username":"juan",
    "password":"perez"
}
```

VULNERABLE A 

```
POST /login HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 57

{
    "username":"' OR 1=1;-- ",
    "password":""
}
```

```
POST /register HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 52

{
    "username":"juan",
    "password":"perez"
}
```
#### POST passwords

POST /password?token=token HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 90

{
    "app_username": "alejo",
    "password": "password",
    "app_name": "twitter"
}
```

#### GET passwords

```
GET /password?token=token&app_name=appname HTTP/1.1
Host: localhost:5000
```

