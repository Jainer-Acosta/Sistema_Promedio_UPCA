from flask import *

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def inicio():
    
    nota_final = None
    estado = None
    
    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        parcial = float(request.form["parcial"])
    
        porcentaje_nota = 0.25
        porcentaje_parcial = 0.50
        
        resultado = nota1*(porcentaje_nota) + nota2 *(porcentaje_nota) + parcial *(porcentaje_parcial)
        nota_final = f"{resultado:.1f}"

        if resultado >= 2.95:
            estado = "Aprobaste"
        else:
            estado = "Reprobaste"
        
        
    return render_template("index.html", nota_final=nota_final, estado=estado)

if __name__ == "__main__":
    app.run(debug=True)

