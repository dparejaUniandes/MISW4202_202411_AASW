from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from parametros de salud</p>"

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)