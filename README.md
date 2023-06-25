## Vulnerable API - [86.36/66.69] Criptografia y Seguridad Informatica
---
Esta API ha sido creada con propósitos educativos y tiene como objetivo mostrar diversas vulnerabilidades que pueden ser explotadas por terceros interesados en afectarla. Algunos ejemplos de ataques y vulnerabilidades que se presentan incluyen:

| **_Vulnerabilidad_**     |
|--------------------|
| SQL Injection      |
| CSRF               |
| XSS                |
| CORS               |
| Text Plain Cookie  |


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


## Desarrollo Local

#### Backend

El backend se encuentra desarrollado en el el lenguaje python

Dependencias

| Dependency                   | Version     |
|------------------------------|-------------|
| fastapi                      | 0.95.2      |
| pycparser                    | 2.21        |
| pydantic                     | 1.10.8      |
| requests                     | 2.31.0      |
| uvicorn                      | 0.22.0      |

```shell
python version >= 3.8
# inicializar el servidor backend
python backend/main.py

# terminar servidor backend 
ctrl -C
```
#### Frontend

Este proyecto fue generado con [Angular CLI](https://github.com/angular/angular-cli) version ``15.2.7``.

Ejecute `ng serve` para un servidor de desarrollo. Navegue a `http://localhost:4200/`.La aplicación se recargará automáticamente si cambia alguno de los archivos de origen.

## Desarrollo Docker
```bash
# inicializar el servidor backend
$ docker pull alejovillores/vulnerable-api-rest-backend:latest
$ docker run -it --rm --name vulnerable-api-rest alejovillores/vulnerable-api-rest-backend
```

```bash
# inicializar el servidor frontend
$ docker pull alejovillores/vulnerable-api-rest-front:latest
$ docker run -it --rm --name vulnerable-api-rest alejovillores/vulnerable-api-rest-front
# Cuando pregunta por y/N poner N
```

## Endpoints

#### POST users

```
POST /login HTTP/1.1
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

All passwords
```
GET /passwords HTTP/1.1
Host: localhost:5000
Cookie: token="alejo?True"
```

Password by ``app_name``
```
GET /password?app_name=facebook HTTP/1.1
Host: localhost:5000
Cookie: token="alejo?True"
```

