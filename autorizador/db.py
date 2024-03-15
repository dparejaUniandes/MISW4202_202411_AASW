from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    db.init_app(app)