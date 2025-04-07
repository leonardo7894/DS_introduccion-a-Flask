from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chau")
def chau():
    return "<p>Chau</p>"
