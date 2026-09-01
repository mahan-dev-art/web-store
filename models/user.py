from sqlalchemy import *
from config import db

class User(db.Model):
    __tablename__ =  "users"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String , unique=True , nullable=False , index=True)
    password = Column(String , nullable=False , index=True)
    phone = Column(String , nullable=False , index=True)
    address = Column(String , nullable=False , index=True)