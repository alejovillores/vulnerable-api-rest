FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 5000

CMD poetry run uvicorn backend.main:app --host 0.0.0.0