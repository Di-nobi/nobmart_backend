from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status, Request
from app.utils.oauth_utils import create_access_token, decode_access_token
from app.database import store

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db_store = store
class NewUser(BaseModel):
    email: str
    password: str


class User(BaseModel):
    email: str
    is_active: Optional[bool]

    class Config:
        from_attributes = True

# class NewProduct(BaseModel):
    # name: str
    # description: str
    # price: float


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        from_attributes = True

class BlockchainTransaction(BaseModel):
    id: str
    transaction_id: str
    user_id: str
    product_id: str
    status: str

    class Config:
        from_attributes = True

class NewOrder(BaseModel):
    product_id: str
    status: str

class WalletConnectRequest(BaseModel):
    address: str

class TransactionRequest(BaseModel):
    wallet_address: str
    private_key: str
    value: str

class TokenData(BaseModel):
    email: str = None


async def get_current_user(request: Request):
    cred_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    auth_header = request.headers.get("Authorization")
    if auth_header is None or not auth_header.startswith("Bearer "):
        raise cred_exception

    token = auth_header.split(" ")[1]
    payload = decode_access_token(token)
    id: str = payload.get("sub")
    if id is None:
        raise cred_exception
    
    usr = db_store.get_user_id(id)
    if not usr:
        raise HTTPException(status_code=401, detail='Invalid user')
    
    return id
    