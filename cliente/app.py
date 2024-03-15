from flask import Flask, request
from user import User
from services import login

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! from cliente</p>"

@app.route("/iniciar-experimento")
def start_proof_of_concept():
    # create users
    user1 = User("user1", "pwd1", "", "Colombia", "M", 31)
    user2 = User("user2", "pwd2", "", "Panama", "F", 38)

    # login
    token1 = login(user1)
    user1.update_token(token1)

    token2 = login(user2)
    user2.update_token(token2)

    # update simulation