from sqlalchemy import *
from config import db
import config

class Payment(db.Model):
    __tablename__ =  "payments"
    id = Column(Integer , primary_key=True , index=True)
    status = Column(String , default="pending")
    price = Column(Integer)
    date_created = Column(String(15) , default=config.get_current_time)
    token = Column(String , index=True)
    refid = Column(String , index=True)
    transaction_id = Column(String , index=True)
    card_pan = Column(String , index=True)
    cart_id = Column(Integer , ForeignKey('carts.id') , nullable=False , index=True)
    cart = db.relationship('Cart' , backref = 'payments')