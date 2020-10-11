FROM python:3.7-alpine
LABEL maintainer Nyior Clement

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt 

RUN mkdir /backend
WORKDIR /backend

COPY . /backend

RUN adduser -D user

USER user

# run development server
# CMD python manage.py runserver 0.0.0.0:$PORT
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 30 backend.wsgi