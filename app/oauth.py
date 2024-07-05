from authlib.integrations.starlette_client import OAuth
from fastapi import Depends, FastAPI, HTTPException, status
from starlette.middleware.sessions import SessionMiddleware
from app.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, SECRET_KEY, TWITTER_API_KEY, TWITTER_API_SECRET_KEY

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


oauth = OAuth()

oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    refresh_token_params=None,
    client_kwargs={'scope': 'openid profile email'},
)

oauth.register(
    name='twitter',
    client_id=TWITTER_API_KEY,
    client_secret=TWITTER_API_SECRET_KEY,
    access_token_url='https://api.twitter.com/oauth/access_token',
    access_token_params=None,
    authorize_url='https://api.twitter.com/oauth/authenticate',
    authorize_params=None,
    client_kwargs={'scope': 'email'},
)