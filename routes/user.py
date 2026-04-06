from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import database_models, schemas
from auth import hash_password, create_access_token, verify_password

router = APIRouter()
@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    db_user = database_models.User(user_name=user.username,name = user.name, email=user.email, password = hashed_password, role = "user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: schemas.Login, db: Session = Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.user_name == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        return {"message": "Invalid username or password"}
    access_token = create_access_token(data={"sub": str(db_user.user_name)})
    return {"access_token": access_token, "token_type": "bearer"}

