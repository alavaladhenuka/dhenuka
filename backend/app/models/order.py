from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, index=True)
    requested_qty = Column(Integer, default=1)
    distance_km = Column(Float, default=10.0)
    priority = Column(String, default="MEDIUM")
    status = Column(String, default="PENDING")