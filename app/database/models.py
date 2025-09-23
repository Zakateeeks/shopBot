from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(String, unique=True)
    tg_name = Column(String)
    contact_name = Column(String)
    contact_phone = Column(String)
    contact_address = Column(String)
    order_id = Column(JSONB, unique=True)
    basket = Column(JSONB)
    is_admin = Column(Boolean)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_id = Column(String, unique=True)
    order_name = Column(String)
    order_status = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    price = Column(Integer)
    photo = Column(String)
    description = Column(String)
    category = Column(String)
    name = Column(String)
