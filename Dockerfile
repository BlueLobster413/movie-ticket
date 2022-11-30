FROM python:3.10.8

EXPOSE 80
EXPOSE 8000

ENV PYTHONNUNBUFFERED 1
ENV LISTEN_PORT=8000

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app