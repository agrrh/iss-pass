FROM python:3-slim

COPY requirements.txt /code/requirements.txt
WORKDIR /code

RUN pip install -r requirements.txt

COPY . /code

ENV PYTHONUNBUFFERED=1

CMD python3 daemon.py
