from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    real_name: str
    surname: str
    dob: str
    gender: str
    weight: int
    height: int
    tel: str
    email: str
    password: str
    confirmpassword: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData (BaseModel):
    username: Optional[str] = None
