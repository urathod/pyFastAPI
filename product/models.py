from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String, index=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    Seller = relationship("Seller", back_populates="products")

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    products = relationship("Product", back_populates="Seller")