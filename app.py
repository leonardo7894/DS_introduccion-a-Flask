from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chau")
def chau():
    return "<p>Chau</p>"

@app.route("/hola/<string:nombre>")#string necesita un string
def nombre(nombre):
    return f"<p>hola {nombre}</p>"

@app.route("/tirar-dado/<int:caras>") #int si o si necesita un numero
def dado(caras):
    from random import randint
    h = randint(1, caras)
    return f"<p>tire un  dado de {caras}, salio {h}</p>"

#siempre que haya un string,float,int, en la ruta, quiere decir que necsesita recibir algo y se separa po0r barras '/'