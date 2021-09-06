import os
from fastapi import FastAPI
import psycopg2
import uvicorn

app = FastAPI()

db_user = os.environ.get('DB_USER', 'postgres')
db_pass = os.environ['DB_PASS']
db_name = os.environ.get('DB_NAME', 'postgres')
db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
cloud_sql_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]
db_host = "{}/{}".format(db_socket_dir, cloud_sql_connection_name)

if os.environ["ENV"].lower() == 'dev':
    db_host = "127.0.0.1"

def get_politicians():
    conn = psycopg2.connect(dbname=db_name, 
                            host=db_host, 
                            user=db_user, 
                            password=db_pass, 
                            connect_timeout=30)
    cur = conn.cursor()
    cur.execute("select * from politicians;")
    return cur.fetchone()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/politicians")
async def get_politicians_endpoint():
    return get_politicians()
