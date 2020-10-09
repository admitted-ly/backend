FROM python:3.7-alpine
LABEL naintainer Nyior Clement

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend

COPY . /app

RUN adduser -D user

USER user