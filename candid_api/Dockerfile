FROM python:3.8

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV DB_USER postgres
ENV DB_NAME postgres
ENV ENV dev
ENV CLOUD_SQL_CONNECTION_NAME scenic-cedar-324901:us-west1:candid-postgresql

RUN pip3 install --no-cache-dir -r requirements.txt

CMD gunicorn test_fastapi:app -c gunicorn_config.py
