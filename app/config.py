import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("sqlite:///test.db")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")