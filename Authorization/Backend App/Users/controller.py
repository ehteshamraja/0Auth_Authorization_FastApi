from sqlalchemy.orm import Session

from . import models, schemas
from typing import List

from fastapi import APIRouter,Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)





def create_user(db: Session, user: schemas.User):
    hashed_password = user.password + "notreallyhashed"
    first_name=user.first_name
    last_name=user.last_name
    db_user = models.User(email=user.email, first_name=user.first_name, last_name=user.last_name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
    
