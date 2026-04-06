from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import database_models, schemas
from dependencies import get_current_user

router = APIRouter()
@router.get("/")
def get_product(db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    return db.query(database_models.Product).all()

@router.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    return db.query(database_models.Product).filter(database_models.Product.product_id == product_id).first()

@router.post("/add_product")
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    if db.query(database_models.User).filter(database_models.User.user_name == user.user_name).first().role != "admin":
        return {"message": "Unauthorized"}
    db_product = database_models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/delete_product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db),user: database_models.User = Depends(get_current_user)):
    if db.query(database_models.User).filter(database_models.User.user_name == user.user_name).first().role != "admin":
        return {"message": "Unauthorized"}
    db_product = db.query(database_models.Product).filter(database_models.Product.product_id == product_id).first()
    if not db_product:
        return {"message": "Product not found"}
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

@router.put("/update_product/{product_id}")
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db), user: database_models.User = Depends(get_current_user)):
    if db.query(database_models.User).filter(database_models.User.user_name == user.user_name).first().role != "admin":
        return {"message": "Unauthorized"}
    db_product = db.query(database_models.Product).filter(database_models.Product.product_id == product_id).first()
    if not db_product:
        return {"message": "Product not found"}
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product