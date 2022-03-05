FROM python:alpine

RUN pip install ecdsa \
    pip install bech32;

COPY /wallet /wallet

WORKDIR /wallet
