from flask import *
from blueprints.general import app as general
from blueprints.admin import app as admin
from blueprints.user import app as user
import config
from config import db
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET_KEY   
csrf = CSRFProtect(app)

db.init_app(app)


with app.app_context():
    db.create_all()

if __name__ == "__main__" :
    app.run(debug=True)