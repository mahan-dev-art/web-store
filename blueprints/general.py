from flask import *

app = Blueprint("general" , __name__)

@app.route("/")
def main():
    return "hello"

@app.route("/about")
def about():
    return "hello"

