from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    name: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class ProductCreate(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    quantity: int

class CartCreate(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    quantity: int
