from sqlalchemy.orm import Session

from . import models, schemas
from typing import List

from fastapi import APIRouter,Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine
from passlib.context import CryptContext

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.User):
    hashed_password = get_password_hash(user.password)
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
    
