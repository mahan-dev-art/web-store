from flask import *
from models.product import Product
from models.cart import Cart
from models.cart_item import CartItem
from config import db


app = Blueprint("admin" , __name__)

@app.before_request
def before_request():
    if session.get('admin_login' , None) == None and request.endpoint != 'admin.login':
        abort(403)

@app.route("/admin/login" , methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username' , None)
        password = request.form.get('password' , None)
        
        if username == "admin" and password == "1234":
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")
    else:
        return render_template("admin/login.html")
    
@app.route("/admin/dashboard" , methods=["GET"])
def dashboard():
    carts = Cart.query.filter(Cart.status != "pending").all()
    cart_items = CartItem.query.all()
    return render_template("admin/dashboard.html" , carts = carts)
@app.route("/admin/dashboard/order/<id>" , methods=["GET" , "POST"])
def order(id):
    cart = Cart.query.filter(Cart.id == id).first_or_404()
    if request.method == "GET":
        return render_template("admin/order.html" , cart = cart)
    else:
        status = request.form.get("status")
        
        cart.status = status
        
        db.session.commit()
        
        return redirect(url_for('admin.order' , id=id))    
        
        
@app.route("/admin/dashboard/products" , methods=["GET" , "POST"])
def products():
    if request.method == "GET":
        products = Product.query.all()
        return render_template("admin/products.html" , products=products)

    name = request.form.get("name" , None)
    description = request.form.get("description" , None)
    price = request.form.get("price" , None)
    active = request.form.get("active" , None)
    file = request.files.get("cover" , None)

    p = Product(name=name, description=description, price=int(price), active=1 if active is not None else 0)
    db.session.add(p)
    db.session.commit()

    file.save(f"static/cover/{p.id}.png")
    return redirect("/admin/dashboard/products")


@app.route("/admin/dashboard/edit-product/<int:id>" , methods=["GET" , "POST"])
def edit_product(id):
    product = Product.query.filter(Product.id == id).first_or_404()

    if request.method == "GET":
        return render_template("admin/edit_product.html" , product=product)

    file = request.files.get("cover" , None)
    
    product.name = request.form.get("name" , None)
    product.description = request.form.get("description" ,None)
    product.price = request.form.get("price" , None)
    if request.form.get("active") == None:
        product.active = 0
    else:
        product.active = 1

    db.session.commit()

    if file.filename != "":
        file.save(f'static/cover/{id}.png')
    
    return redirect(url_for("admin.products" , id=id))