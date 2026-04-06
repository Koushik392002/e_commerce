from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    user_name = Column(String(255), primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    role = Column(String(255))

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)

class Cart(Base):
    __tablename__ = "cart"

    user_name = Column(String(255), primary_key=True)
    product_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    user_name = Column(Integer)
    total_amount = Column(Float)    
    status = Column(String(255))
