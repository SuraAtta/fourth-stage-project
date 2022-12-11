from ninja import Schema
from pydantic import EmailStr, Field

class FourOFourOut(Schema):
    detail: str

