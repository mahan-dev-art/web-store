from flask import *
from models.product import Product

app = Blueprint("general" , __name__)

@app.route("/")
def main():
    products = Product.query.all()
    return render_template("index.html" , products = products)

@app.route("/about")
def about():
    return render_template("about.html")

