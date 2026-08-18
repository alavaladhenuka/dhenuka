from pydantic import BaseModel
from typing import Optional

class InventoryCreate(BaseModel):
    sku: str
    name: str
    category: str
    quantity: int
    location: str
    reorder_level: Optional[int] = 10

class InventoryResponse(InventoryCreate):
    id: int

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    order_number: str
    customer_name: str
    items_count: int
    priority: Optional[str] = "Normal"

class OrderResponse(OrderCreate):
    id: int
    status: str

    class Config:
        from_attributes = True