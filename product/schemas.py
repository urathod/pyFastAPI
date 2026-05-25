from typing import Optional

from pydantic import BaseModel, constr

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str = None


class DisplaySeller(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
        
class DisplayProduct(BaseModel):
    id: int
    name: str
    description: str = None
    Seller : DisplaySeller

    class Config:
        orm_mode = True

class Seller(BaseModel):
    id: int
    username: str
    email: str
    password: str # constr(max_length=72)

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None