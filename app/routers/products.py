from fastapi import APIRouter, Depends, HTTPException, Request
from app.schemas import Product, get_current_user
# from app.schemas import User
from app.models.user import User
from app.database import store
from app.routers.users import login_user
router = APIRouter()
db_store = store

@router.get('/products')
async def get_products(current_user: str = Depends(get_current_user)):
    """Returns all products in the database"""
    usr = db_store.get_user_id(current_user)
    if not usr:
        raise HTTPException(status_code=401, detail='Invalid user')
    all_products = db_store.get_all_products()
    if not all_products:
        raise HTTPException(status_code=404, detail='No products found')
    prods = [count for count in all_products]
    return {'All products': prods}

@router.get('/products/{product_id}')
async def get_a_product(product_id: str, current_user: str = Depends(get_current_user)):
    """Returns a product with the given id"""
    usr = db_store.get_user_id(current_user)
    if not usr:
        raise HTTPException(status_code=401, detail='Invalid user')
    product = db_store.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    prod_info = {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    }
    return {'Product': prod_info}

@router.post('/products')
async def new_product(product: Product, current_user: User = Depends(get_current_user)):
    usr = db_store.get_user_id(current_user)
    if not usr:
        raise HTTPException(status_code=401, detail='Invalid user')
    if product.name is None or product.description is None or product.price is None or product.quantity is None:
        raise HTTPException(401, detail="Missing Key informations for product")
    new_prod = {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity,
        'user_id': current_user
    }
    create_a_product = db_store.add_product(**new_prod)
    return {'message': f'{create_a_product.name} with id: {create_a_product.id} is successfully created'}