FROM python:latest

ADD Servidor.py /servidor/
ADD proto /servidor/proto
WORKDIR /servidor/

RUN pip install --upgrade pip && \
    pip install grpcio && \
    pip install grpcio-tools

EXPOSE 12000