from ninja import Schema
from pydantic import EmailStr, Field


class AccountIn(Schema):
    username: str = Field(min_length=1)
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str = Field(min_length=8)



class TokenOut(Schema):
    access: str


class AccountOut(Schema):
    id: int
    username: str
    email: EmailStr


class AuthOut(Schema):
    token: TokenOut
    account: AccountOut


class SigninIn(Schema):
    email: EmailStr
    password: str
