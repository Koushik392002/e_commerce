from fastapi import FastAPI
from database import engine
import database_models
from routes import user, products, cart, order

database_models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user.router, prefix="/users")
app.include_router(products.router, prefix="/products")
app.include_router(cart.router, prefix="/cart")
app.include_router(order.router, prefix="/orders")