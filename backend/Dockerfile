FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 5000

CMD uvicorn main:app --host 0.0.0.0 --port 5000 --log-level info