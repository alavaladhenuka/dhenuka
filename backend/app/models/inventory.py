import enum
from sqlalchemy import Column, Integer, String, Float, Date, Enum
from app.db.base import Base

class QualityStatus(str, enum.Enum):
    GOOD = "GOOD"
    DAMAGED = "DAMAGED"

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    product_code = Column(String, unique=True, index=True, nullable=False)
    quantity = Column(Integer, default=0)
    quality = Column(Enum(QualityStatus), default=QualityStatus.GOOD)
    expiry_date = Column(Date, nullable=False)
    aisle_location = Column(String, nullable=True)
    discount_percentage = Column(Float, default=0.0)