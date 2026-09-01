from flask import *

app = Blueprint("user" , __name__)

@app.route("/user")
def user():
    return "hello"