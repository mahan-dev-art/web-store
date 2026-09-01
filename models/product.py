from sqlalchemy import *
from config import db

class Product(db.Model):
    __tablename__ =  "products"
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String , unique=True , nullable=False , index=True)
    description = Column(String, nullable=False , index=True)
    price = Column(Integer , nullable=False , index=True)
    active = Column(Integer , nullable=False , index=True)