from sqlalchemy import *
from sqlalchemy.orm import *
from config import db

class CartItem(db.Model):
    __tablename__ =  "cart_items"
    id = Column(Integer , primary_key=True , index=True)
    status = Column(String , default="pending")
    product_id = Column(Integer , ForeignKey('products.id') , nullable=False , index=True)
    cart_id = Column(Integer , ForeignKey('carts.id') , nullable=False , index=True)
    quantity = Column(Integer)
    price = Column(Integer)
    
    product = db.relationship("Product" , backref = 'cart_items')
    cart = db.relationship("Cart" , backref = backref('cart_items' , lazy = 'dynamic'))