from flask import *
from models.product import Product

app = Blueprint("general" , __name__)

@app.route("/")
def main():
    products = Product.query.filter(Product.active == 1).all()
    return render_template("index.html" , products = products)

@app.route("/product/<int:id>/<name>")
def product(id , name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("product.html" , product = product)

@app.route("/about")
def about():
    return render_template("about.html")

