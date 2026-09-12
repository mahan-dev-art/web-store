from flask import *
from blueprints.general import app as general
from blueprints.admin import app as admin
from blueprints.user import app as user
import config
from config import db
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from models.user import User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET_KEY   

csrf = CSRFProtect(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    flash("لطفا اول وارد حساب کاربری تان بشوید")
    return redirect(url_for("user.login"))

@app.context_processor
def inject_dict_for_all_templates():
    return dict(my_config=config)

with app.app_context():
    db.create_all()

if __name__ == "__main__" :
    app.run(debug=True , host="0.0.0.0")