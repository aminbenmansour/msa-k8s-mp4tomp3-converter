FROM python:3.11-slim-bulleyes

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essentils default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app

EXPOSE 5000

CMD ["python3", "server.py"]