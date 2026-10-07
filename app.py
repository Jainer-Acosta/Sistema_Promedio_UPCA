from flask import *

app = Flask(__name__)
@app.route("/")
def inicio():
    return "Sistema de Notas "

if __name__ == "__main__":
    app.run(debug=True)





