from flask import *
import models.user

app = Blueprint("user" , __name__)

@app.route("/user")
def user():
    return "hello"