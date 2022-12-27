from sqlalchemy.orm import Session

from . import models, schemas
from typing import List

from fastapi import APIRouter,Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas

from .controller import *



api = APIRouter(
    prefix="/v1/users",
    responses={404: {"description": "Not found"}},
)


@api.post("/users/", tags=["User"] , response_model=schemas.User)
def sign_up(user: schemas.User, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
