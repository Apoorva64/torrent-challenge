FROM python:3.10-bookworm

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt


COPY src /app/src

CMD ["python", "/app/src/main.py"]