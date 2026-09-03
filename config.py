from flask_sqlalchemy import SQLAlchemy
import time

SECRET_KEY = "gfdgjsdbjcbsdugcsdbcfalavcdb654354"
SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
db = SQLAlchemy()

def get_current_time():
    return round(time.time())

