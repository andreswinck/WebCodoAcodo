from flask import Flask

app = Flask(__name__)

@app.route("/")
def iniciar():
    return "<h1>Servidor On Line</h1>"

@app.route("/mensajes")
def mostrar_mensajes():
    return "<h1>Lista de mensajes</h1>"


if __name__ == "__main__":
    app.run(debug=True)
