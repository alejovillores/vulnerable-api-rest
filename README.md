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

Desde el directorio *backend*

```bash
# inicializar el servidor backend
$ make run-server
```

Desde el directorio *frontend*

```bash
# inicializar el cliente frontend
$ make run-client
# Cuando pregunta por y/N poner N
```

## Endpoints

Se agregan los endpoints que muestran vulnerabilidad para que se vea que al correrlos no muestra las vulnerabilidades

#### POST users

```bash
curl --location 'localhost:5000/login' \
--header 'Content-Type: application/json' \
--data '{
    "username":"usuario2",
    "password":"password"
}'
```
####  Vulnerable a injeccion SQL

```bash
curl --location 'localhost:5000/login' \
--header 'Content-Type: application/json' \
--data '{
    "username":"' OR 1=1;-- ",
    "password":"password"
}'
```


```bash
curl --location 'localhost:5000/register' \
--header 'Content-Type: application/json' \
--data '{
    "username":"usuario",
    "password":"password"
}'
```
#### POST reset passwords

```bash
curl --location 'localhost:5000/password/reset' \
--header 'Cookie: token=<token>'
--data '{
    "new_password":"password"
}'
```
#### POST passwords

```bash
curl --location 'localhost:5000/password' \
--header 'Content-Type: application/json' \
--header 'Cookie: token=<token>' \
--data '{
    "app_username": "usuario",
    "password": "password",
    "app_name": "facebook"
}'
```

#### GET passwords

All passwords
```bash
curl --location 'localhost:5000/passwords' \
--header 'Cookie: token=<token>'
```

Password by ``app_name``
```bash
curl --location 'localhost:5000/password?app_name=fac' \
--header 'Cookie: token=<token>'
```

#### Vulnerable to SQL Injection

Obtener todo las contraseñas de los usuarios
```bash
curl --location 'localhost:5000/password?app_name=%27%20OR%201%3D1%3B%20--' \
--header 'Cookie: token=<token>'
```


