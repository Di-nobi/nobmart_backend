from fastapi import APIRouter, Depends, HTTPException
from app.schemas import NewUser
from app.schemas import User
from app.database import store
from app.utils.oauth_utils import create_access_token
router = APIRouter()
db_store = store
@router.post('/signup', response_model=None)
async def create_user(user: NewUser):

    if user.email is None or user.password is None:
        raise HTTPException(status_code=401, detail='Missing email or password')
    chk_usr = db_store.get_user_by_email(user.email)
    if chk_usr:
        raise HTTPException(status_code=401, detail='User already exists')
    create_a_user = db_store.add_user(**user.model_dump())
    return {'message': f'{create_a_user.email} created successfully'}

@router.post('/login', response_model=dict)
async def login_user(user: NewUser):
    if user.email is None or user.password is None:
        raise HTTPException(status_code=401, detail='Missing email or password')
    usr = db_store.get_user_by_email(user.email)
    if not usr:
        raise HTTPException(status_code=401, detail='Invalid email or password')
    if not usr.verify_password(user.password):
        raise HTTPException(status_code=401, detail='Invalid email or password')
    access_token = create_access_token(data={'sub': usr.id}, expires_delta=1)
    return {'message': f'{usr.email} is logged in with access token {access_token}'}

