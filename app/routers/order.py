from .. import schemas, models
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends, HTTPException, status, APIRouter
from ..database import get_db


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.OrderResponse)
def create_order(order: schemas.CreateOrderSchema, db: Session = Depends(get_db)):
    total_amount = 0
    new_order = models.Order(total_amount=total_amount)
    db.add(new_order)
    
    for product in order.products:
        _product_db = db.query(models.Product).filter(models.Product.id == product.id).first()
        new_order_detail = models.OrderDetail(
            order = new_order,
            product = _product_db,
            quantity = product.quantity,
            unit_price = product.unit_price
        )
        db.add(new_order_detail)
        total_amount += product.quantity * product.unit_price
    
    new_order.total_amount = total_amount
    db.commit()

    # Transaction
    products_to_ship = db.query(models.OrderDetail).filter(models.OrderDetail.order_id == new_order.id)
    for product in products_to_ship:
        ordered_product = db.query(models.Product).filter(models.Product.id == product.product_id).first()
        ordered_product.stock -= product.quantity
    
    new_order.shipped = True
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get('/', response_model=schemas.ListOrderResponse)
def get_orders(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    orders = db.query(models.Order).limit(limit).offset(skip).all()
    return {
        'status': 'success',
        'results': len(orders),
        'orders': orders
    }


@router.get('/{id}', response_model=schemas.OrderDetailResponse)
def get_order_detail(id: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).options(joinedload(models.Order.order_details)).filter(models.Order.id == id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order Not Found')
    return order
