from sqlalchemy import *
from config import db
from flask_login import UserMixin
import config

class User(db.Model , UserMixin):
    __tablename__ =  "users"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String , unique=True , nullable=False , index=True)
    password = Column(String , nullable=False , index=True)
    date_created = Column(String(15) , default=config.get_current_time)
    phone = Column(String , nullable=False , index=True)
    address = Column(String , nullable=False , index=True)