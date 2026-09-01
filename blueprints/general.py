from flask import *

app = Blueprint("general" , __name__)

@app.route("/")
def home():
    return "hello"