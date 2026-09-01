from flask import *

app = Blueprint("admin" , __name__)

@app.route("/admin")
def admin():
    return "hello"