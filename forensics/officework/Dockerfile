FROM python:3.10

RUN pip install flask gunicorn

COPY . /app
WORKDIR /app

CMD gunicorn --bind 0.0.0.0:5000 app:app