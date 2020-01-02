FROM python:latest

ADD Cliente.py /cliente/
ADD proto /cliente/proto
ADD Dummy.py /cliente/

RUN pip install --upgrade pip && \
    pip install grpcio && \
    pip install grpcio-tools

WORKDIR /cliente/