from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
db = SQLAlchemy()