from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
import database_models, schemas
from dependencies import get_current_user

router = APIRouter()
@router.post("/add_to_cart")
def add_to_cart(cart_item: schemas.CartCreate, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    db_cart_item = database_models.Cart(user_name=user.user_name, product_id=cart_item.product_id,name = cart_item.name, description = cart_item.description, price = cart_item.price, quantity=cart_item.quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

@router.get("/cart")
def view_cart(db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    return db.query(database_models.Cart).filter(database_models.Cart.user_name == user.user_name).all()

@router.delete("/remove_from_cart/{product_id}")
def remove_from_cart(product_id: int, db: Session = Depends(get_db),user: database_models.User = Depends(get_current_user)):
    db_cart_item = db.query(database_models.Cart).filter(database_models.Cart.user_name == user.user_name, database_models.Cart.product_id == product_id).first()
    if not db_cart_item:
        return {"message": "Item not found in cart"}
    db.delete(db_cart_item)
    db.commit()
    return {"message": "Item removed from cart successfully"}

