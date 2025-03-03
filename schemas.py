from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str


class ReadUsers(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str

    class Config:
        from_attributes = True

