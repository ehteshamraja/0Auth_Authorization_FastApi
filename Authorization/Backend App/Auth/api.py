from datetime import datetime, timedelta
from typing import Union

from fastapi import APIRouter,Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from .utils import *
from Users.schemas import User as UserDB
from Users.models  import User as UserModel








api = APIRouter(
    prefix="/v1/users",
    responses={404: {"description": "Not found"}},
)





@api.post("/token", tags=["Auth"] ,response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = authenticate_user(db.query(UserModel).all(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}




