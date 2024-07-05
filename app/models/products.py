from . import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import uuid

class Product(Base):
    __tablename__ = 'products'
    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    user_id = Column(String(255), ForeignKey("users.id"))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    user = relationship('User', back_populates='products')

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        self.quantity = kwargs.get('quantity')
        self.user_id = kwargs.get('user_id')
    
    def deduct_quantity(self, quantity):
        if len(self.quantity) == 0:
            return None
        else:
            self.quantity -= quantity
        return self.quantity
    
    