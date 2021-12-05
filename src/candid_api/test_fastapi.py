from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db import models
from db.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_politicians(db: Session):
    return db.query(models.Politician).all()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/politicians")
async def get_politicians_endpoint(db: Session = Depends(get_db)):
    return get_politicians(db)
