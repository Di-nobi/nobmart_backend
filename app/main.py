from fastapi import FastAPI
from app.routers import auth, orders, products, transactions, users, blockchain
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 
# app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
# app.include_router(orders.router, prefix='/api/orders', tags=['orders'])
app.include_router(products.router, tags=['products'])
# app.include_router(transactions.router, prefix='/api/transactions', tags=['transactions'])
app.include_router(users.router, tags=['users'])
# app.include_router(blockchain.router)