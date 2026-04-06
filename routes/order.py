from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
import database_models, schemas
from dependencies import get_current_user

router = APIRouter()
@router.get("/orders")
def get_orders(db: Session = Depends(get_db),user: database_models.User = Depends(get_current_user)):
    return db.query(database_models.Order).filter(database_models.Order.user_id == user.user_id).all()

@router.post("/place_order")
def place_order(db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    cart_items = db.query(database_models.Cart).filter(database_models.Cart.user_name == user.user_name).all()
    if not cart_items:
        return {"message": "Cart is empty"}
    total_price = sum(item.price * item.quantity for item in cart_items)
    new_order = database_models.Order(user_name=user.user_name, total_amount=total_price, status="placed")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order placed successfully"}

@router.get("/orders/{order_id}")
def get_order_by_id(order_id: int, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    order = db.query(database_models.Order).filter(database_models.Order.order_id == order_id, database_models.Order.user_name == user.user_name).first()
    if not order:
        return {"message": "Order not found"}
    return order

@router.put("/orders/{order_id}/cancel")
def cancel_order(order_id: int, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    order = db.query(database_models.Order).filter(database_models.Order.order_id == order_id, database_models.Order.user_name == user.user_name).first()
    if not order:
        return {"message": "Order not found"}
    if order.status not in ["placed", "order placed", "shipped", "delivered"]:
        return {"message": "Only placed orders can be canceled"}
    order.status = "canceled"
    db.commit()
    return {"message": "Order canceled successfully"}

@router.put("/orders/{order_id}/{status}")
def update_order_status(order_id: int, status: str, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    order = db.query(database_models.Order).filter(database_models.Order.order_id == order_id, database_models.Order.user_name == user.user_name).first()
    if not user.role == "admin":
        return {"Unauthorized"}
    if status not in ["placed", "shipped", "delivered", "canceled"]:
        return {"message": "Invalid status"}
    order.status = status
    db.commit()
    return {"message": "Order status updated successfully"}