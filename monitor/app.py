from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from services import watch_dog
from modelos import init_db, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)    
    watch_dog()
