from sqlalchemy.orm import Session

from . import models, schemas
from typing import List

from fastapi import APIRouter,Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Auth.utils import *
from Users.schemas import User as UserDB

from . import models, schemas,controller

from .controller import *

api = APIRouter(
    prefix="/v1/users",
    responses={404: {"description": "Not found"}},
)


@api.post("/signup/", tags=["User"] , response_model=schemas.User)
def sign_up(user: schemas.User, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@api.get("/current_user/", tags=["User"] )
async def current_user(current_user: UserDB = Depends(get_current_active_user)):
    return current_user

