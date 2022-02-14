FROM python:3.8.12-alpine3.14 
LABEL maintainer="Cecchetti"

RUN mkdir /app
WORKDIR /app

# Env vars
ENV PYTHONUNBUFFERED 1

# Installing dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/

RUN apk add postgresql-client
# Django service
EXPOSE 8000


CMD ['runserver', '0.0.0.0:3000']