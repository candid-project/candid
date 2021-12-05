import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PGUSER = os.environ.get("DB_USER", "postgres")
PGPASS = os.environ.get("DB_PASS")
PGNAME = os.environ.get("DB_NAME", "postgres")
PGPORT = os.environ.get("DB_PORT", 5432)
db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
cloud_sql_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]
PGHOST = "{}/{}".format(db_socket_dir, cloud_sql_connection_name)

if os.environ["ENV"].lower() == "dev":
    PGHOST = "127.0.0.1"
    SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
        PGUSER, PGPASS, PGHOST, PGPORT, PGNAME
    )
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@/{}?host={}".format(
        PGUSER, PGPASS, PGNAME, PGHOST
    )

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
