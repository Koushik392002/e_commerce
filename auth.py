from datetime import timedelta, datetime
from jose import jwt
from passlib.context import CryptContext
import hashlib
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\rjaya\Sample\Hello\e_commerce\environment_variables.env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    password = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(password: str, stored_hash: str):
    password = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.verify(password, stored_hash)