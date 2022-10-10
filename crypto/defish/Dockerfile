FROM python:alpine

WORKDIR /app

RUN pip install Flask jinja2

COPY . /app

ENTRYPOINT ["python", "main.py"]

