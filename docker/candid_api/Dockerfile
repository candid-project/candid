FROM python:3.10

ENV PYTHONNUNBUFFERED True

RUN pip install "poetry==1.1.12"

COPY ./poetry.lock /pyproject.toml /
RUN poetry config virtualenvs.create false && \
    poetry install -v --no-interaction --no-ansi --no-root

RUN mkdir /src
COPY ./src /src
WORKDIR /src/candid_api

ENV DB_USER postgres
ENV DB_NAME postgres
ENV ENV dev
ENV CLOUD_SQL_CONNECTION_NAME scenic-cedar-324901:us-west1:candid-postgresql

CMD poetry run gunicorn test_fastapi:app -c gunicorn_config.py
