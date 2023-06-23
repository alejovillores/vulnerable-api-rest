## Vulnerable API - [86.36/66.69] Criptografia y Seguridad Informatica
---
Esta API posee fines educativos, mostrando una API cuya forma de ser desarrollada genera varias vulnerabilidades para ser explotada por un externo que quiera afectarnos. Dentro de estos ataques y vulnerabilidades se encuentran:

* SQL Injection
* CRSF
* XSS
* CORS
* Text Plain Cookie 

### Integrantes del Trabajo Práctico

* [Alejo Villores](https://github.com/alejovillores) 
* [Ignacio Brusati](https://github.com/brusati)
* [Ignacio Iragui](https://github.com/niragui)
* [Santiago Fernandez](https://github.com/safernandezc)

### Fuentes de documentacion

* SQL Injection
    * [OWASP](https://owasp.org/www-community/attacks/SQL_Injection)
    * [PortSwigger](https://portswigger.net/web-security/sql-injection#:~:text=SQL%20injection%20(SQLi)%20is%20a,not%20normally%20able%20to%20retrieve.)
* CRSF
    * [OWASP](https://owasp.org/www-community/attacks/csrf)
* Cross Site Scripting (XSS)
    * [OWASP](https://owasp.org/www-community/attacks/xss/#:~:text=Cross%2DSite%20Scripting%20(XSS),to%20a%20different%20end%20user.)


### Desarrollo Local

```bash
$ python version >= 3.8

# inicializar el servidor backend
python backend/main.py

# terminar servidor backend 
ctrl -C
```



### Desarrollo Docker
```bash
# inicializar el servidor backend

$ docker pull alejovillores/vulnerable-api-rest-backend:latest
$ docker run -it --rm --name vulnerable-api-rest alejovillores/vulnerable-api-rest
```

```bash
# inicializar el servidor frontend
$ docker pull alejovillores/vulnerable-api-rest-front:latest
$ docker run -it --rm --name vulnerable-api-rest alejovillores/vulnerable-api-rest
# Cuando pregunta por y/N poner N
```

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
####  Vulnerable 

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

```
GET /password/reset?new_password=alejovillores HTTP/1.1
Host: localhost:5000
Cookie: token="alejo?True"
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

