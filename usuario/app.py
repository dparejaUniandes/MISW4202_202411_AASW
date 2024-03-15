from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from usuario</p>"

""" Lo que se envia en la peticion desde el cliente
{
                "username": "",
                "token": "",
                "edad": 1,
                "genero": "",
                "pais": "
            }
"""

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)