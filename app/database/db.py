from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import DATABASE_URL
from app.models import Base
from app.models.user import User
from app.models.products import Product

class Database:
    """The Main engine for the backend server"""
    def __init__(self):
        self.__engine = create_engine('sqlite:///test.db', echo=False)
        Base.metadata.create_all(self.__engine)
        self.__session = None
    def begin_session(self):
        session_factory = sessionmaker(bind=self.__engine, autoflush=False)
        self.__session = scoped_session(session_factory)

    def commit(self):
        self.__session.commit()
    
    def get_user_id(self, id):
        usr = self.__session.query(User).filter(User.id == id).first()
        if not usr:
            return None
        return usr
    
    def get_user_by_email(self, email):
        usr = self.__session.query(User).filter(User.email == email).first()
        if not usr:
            return None
        return usr
    
    def add_user(self, **user):
        usr = User(**user)
        self.__session.add(usr)
        self.__session.commit()
        return usr
    
    def add_product(self, **product):
        prod = Product(**product)
        self.__session.add(prod)
        self.__session.commit()
        return prod
    
    def get_all_products(self):
        products = self.__session.query(Product).all()
        if not products:
            return None
        return products
    
    def get_product(self, id):
        product = self.__session.query(Product).filter(Product.id == id).first()
        if not product:
            return None
        return product