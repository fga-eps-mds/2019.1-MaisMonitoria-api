FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk update && \
    apk upgrade && \
    apk add git

RUN apk add --no-cache bash
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000