# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR ./webdemo

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]
