import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (CheckConstraint(
        'stock>=0',
        'stock should exist in the inventory'
        ),)

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    description = Column(String, nullable=False)
    unit_price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    order_details = relationship('OrderDetail', backref='product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    shipped = Column(Boolean(), default=False)
    total_amount = Column(Integer(), nullable=True)
    order_details = relationship('OrderDetail', backref='order')


class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    order_id = Column(UUID, ForeignKey('orders.id'))
    product_id = Column(UUID, ForeignKey('products.id'))
    unit_price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
