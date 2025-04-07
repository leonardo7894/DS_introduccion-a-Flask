from flask import Flask ,url_for

app = Flask(__name__)


@app.route("/")
def main():
    url_hola = url_for("hola")
    url_nombre = url_for("nombre", nombre = "leonardo")
    url_dados = url_for("dado", caras=6)
    url_imagen = url_for("static", filename="logo.jpg")
    url_chau = url_for("chau")
    return f"""
    <a href ="{url_hola}">hola</a>
    <br>
    <a href ="{url_nombre}">nombre</a>
    <br>
    <a href ="{url_dados}">dados</a>
    <br>
    <a href ="{url_imagen}">imagen</a>
    <br>
    <a href ="{url_chau}">chau</a>
"""

@app.route("/hola")
def hola():
    return "<p>hola leonardo</p>"

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

@app.route("/suma/<int:n1>/<int:n2>")#string necesita un string
def suma(n1, n2):
    s= n1+n2
    return f"<p>{n1} + {n2} = {s}</p>"

#siempre que haya un string,float,int, en la ruta, quiere decir que necsesita recibir algo y se separa po0r barras '/'



