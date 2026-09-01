from flask import *

app = Blueprint("admin" , __name__)

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
    if session.get('admin_login' , None) == None :
        abort(403)
    return render_template("admin/dashboard.html")