FROM python:3.12

RUN apt-get update && apt-get install -y gcc libpq-dev curl

WORKDIR /l24
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt