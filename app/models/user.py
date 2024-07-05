from sqlalchemy import Column, Integer, String, Float, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from . import Base
import uuid
from bcrypt import gensalt, hashpw, checkpw
class User(Base):
    __tablename__ = 'users'
    id = Column(String(255), primary_key=True, nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    products = relationship('Product', back_populates='user')

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.email = kwargs.get('email')
        self.password = self.hash_password(kwargs.get('password'))

    def hash_password(self, password: str):
        """Hashes the password"""
        salted_password = gensalt()
        return hashpw(password.encode('utf8'), salted_password)
    
    def verify_password(self, password: str):
        """Verifies the password"""
        return checkpw(password.encode('utf8'), self.password)