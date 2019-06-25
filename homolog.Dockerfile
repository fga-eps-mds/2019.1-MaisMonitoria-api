FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD bash -c "python3 manage.py runserver 0.0.0.0:8000"