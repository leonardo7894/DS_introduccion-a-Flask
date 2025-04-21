from flask import Flask ,url_for, render_template
import sqlite3

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

app = Flask(__name__)


db = None
def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():
    global db
    db.close()
    db = None

@app.route("/test.db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    res = cursor.execute("SELECT count(*) AS cant FROM usuarios")
    res = cursor.fetchone()
    registros = res["cant"]
    cerrarConexion()
    return f"hay {registros} registros en la tabla ususarios"
    
@app.route("/crear_usuario_argumento/<string:usuario>/<string:email>")
def argumento(usuario, email):
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES"
    cursor.execute(consulta,(usuario,email))
    db.commit()
    cerrarConexion()
    return f"registro agregado ({usuario})"

@app.route("/eliminar")
def argumentos():
    pass


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

#siempre que haya un string,float,int, en la ruta, quiere decir que nesesita recibir algo y se separa por barras '/'

@app.route("/mostrar-datos/<int:id>")
def datos(id):
    abrirConexion()
    cursor = db.cursor()
    res = cursor.execute("SELECT id, usuario,email FROM usuarios WHERE id = ?",(id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario=None
    email=None
    if res != None:
        usuario=res["usuario"]
        email=res["email"]
    return render_template("datos.html",usuario=usuario, email=email, id=id)
    
   