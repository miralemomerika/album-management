from .user import UserBase
from pydantic import BaseModel, EmailStr
from typing import Union


class AdminUserCreate(UserBase):
    email: EmailStr
    first_name: str
    last_name: str
    password: str


class AdminUserUpdate(UserBase):
    pass


class AdminUserRead(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str

    model_config = {
        "from_attributes": True,
    }


class AdminUserLogin(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    first_name: str
    last_name: str


class TokenPayload(BaseModel):
    sub: Union[int, None] = None
