FROM python:latest

ADD Cliente.py /cliente/
ADD Dummy.py /cliente/

RUN pip install --upgrade pip && \
    pip install pika

WORKDIR /cliente/