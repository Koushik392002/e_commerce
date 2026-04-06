# E-Commerce API

A simple **FastAPI-based e-commerce backend** that supports user authentication, products, cart, and orders.
## **Features**

- User authentication with JWT (signup/login)
- Product catalog management
- Cart management
- Order placement and tracking
- Environment variable configuration

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Create a .env file (see .env.example):
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Running the API
uvicorn main:app --reload
Open http://127.0.0.1:8000/docs
 to access Swagger UI and explore the API endpoints.

 API Endpoints
Auth
Endpoint	Method	Description
/signup	POST	Register a new user
/login	POST	Login and get JWT token

Products
Endpoint	Method	Description
/products   GET	    List all products
/products/products/{id}	POST	Get single product details
/products/add_product/{id}	POST	Create new product (admin)
/products/delete_product/{id} DELETE Delete a product (admin)
/products/update_product/{id} PUT Update a product(admin)

Cart
Endpoint	Method	Description
/cart/cart	GET	 Get user cart items
/cart/cart/add_to_cart	POST	Add product to cart
/cart/remove_from_cart/{id}	DELETE	Remove product from cart

Orders
Endpoint	Method	Description
/orders/orders	GET	List all orders
/orders/place_orders	POST	Place an order
/orders/orders/{id}	GET	Get order details
/orders/orders/{order_id}/cancel DELETE Cancel an order
/orders/orders/{order_id}/{status} UPDATE Update an order(admin) 

JWT token is required for /cart , /orders and /products endpoints. Pass it in the Authorization header:
Authorization: Bearer <your_token>

Environment Variables
SECRET_KEY – secret key for JWT signing
ALGORITHM – JWT algorithm (e.g., HS256)
ACCESS_TOKEN_EXPIRE_MINUTES – token expiration time in minutes

ecommerce/
├── routes/
│   ├── user.py
│   ├── products.py
│   ├── cart.py
│   └── order.py
├── main.py          # App entry point
├── auth.py          # JWT & hashing logic
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic request/response models
├── .env             # Environment variables
├── .gitignore
└── requirements.txt

License

MIT License © 2026 Koushik



