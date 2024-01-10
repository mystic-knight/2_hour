
from pydantic import BaseModel
from datetime import datetime, timedelta, date
from peewee import *
from typing import List

class RegisterUser(BaseModel):
    user_name: str
    email: str
    password: str = None
    google_id: str = None
    phone_number: str = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None