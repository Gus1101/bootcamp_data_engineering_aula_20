### A responsabilidade deste arquivo é ser o modelo da database

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    supplier_email = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())