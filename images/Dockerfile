FROM python:3.9-slim-buster

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
COPY src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY alembic /epicenter/alembic
COPY bin /epicenter/bin
COPY src /epicenter/src
COPY sql /epicenter/sql
COPY alembic.ini /epicenter/.

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/epicenter/src"

WORKDIR /epicenter
