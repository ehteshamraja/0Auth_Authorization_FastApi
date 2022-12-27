from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str



    class Config:
        orm_mode = True
