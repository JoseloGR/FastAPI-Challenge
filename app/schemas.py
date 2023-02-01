from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, constr

class ProductBaseSchema(BaseModel):
    description: str
    unit_price: int
    stock: int

    class Config:
        orm_mode = True

class CreateProductSchema(ProductBaseSchema):
    pass

class ProductResponse(ProductBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class UpdateProductSchema(BaseModel):
    description: str
    unit_price: int
    stock: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class ListProductResponse(BaseModel):
    status: str
    results: int
    products: List[ProductResponse]

class ItemSchema(BaseModel):
    id: uuid.UUID
    quantity: int
    unit_price: int

class OrderDetailSchema(BaseModel):
    id: uuid.UUID
    order_id: uuid.UUID
    product_id: uuid.UUID
    unit_price: int
    quantity: int

    class Config:
        orm_mode = True

class OrderBaseSchema(BaseModel):
    shipped: bool
    total_amount: int

    class Config:
        orm_mode = True

class CreateOrderSchema(BaseModel):
    products: List[ItemSchema]

class OrderResponse(OrderBaseSchema):
    id: uuid.UUID

class ListOrderResponse(BaseModel):
    status: str
    results: int
    orders: List[OrderResponse]

class OrderDetailResponse(OrderBaseSchema):
    id: uuid.UUID
    order_details: List[OrderDetailSchema]
