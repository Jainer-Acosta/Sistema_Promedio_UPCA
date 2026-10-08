from flask import *

app = Flask(__name__)

app.secret_key = "hola_profe"

@app.route("/", methods=["GET", "POST"])
def inicio():

    nota_final_primera = None
    nota_final_segunda = None
    nota_acumulada = None

   
    if "resultado_primera" in session:
        nota_final_primera = f"{session['resultado_primera']:.1f}"

  
    if "resultado_segunda" in session:
        nota_final_segunda = f"{session['resultado_segunda']:.1f}"


    if request.method == "POST":

        # CALCULAR PRIMER CORTE
        if "nota1_primera" in request.form:

            nota1_primera = float(request.form["nota1_primera"])
            nota2_primera = float(request.form["nota2_primera"])
            parcial_primera = float(request.form["parcial_primera"])

            porcentaje_nota = 0.25
            porcentaje_parcial = 0.50

            resultado_primera = nota1_primera * (porcentaje_nota) + nota2_primera * (porcentaje_nota) + parcial_primera * (porcentaje_parcial)
            
            session["resultado_primera"] = resultado_primera

            nota_final_primera = f"{resultado_primera:.1f}"


        # CALCULAR SEGUNDO CORTE
        if "nota1_segunda" in request.form:

            nota1_segunda = float(request.form["nota1_segunda"])
            nota2_segunda = float(request.form["nota2_segunda"])
            parcial_segunda = float(request.form["parcial_segunda"])

            porcentaje_nota = 0.25
            porcentaje_parcial = 0.50

            resultado_segunda = nota1_segunda * (porcentaje_nota) + nota2_segunda * (porcentaje_nota) + parcial_segunda * (porcentaje_parcial)
            
            session["resultado_segunda"] = resultado_segunda

            nota_final_segunda = f"{resultado_segunda:.1f}"
            
        if "resultado_primera" in session and "resultado_segunda" in session:
            
            acumulada = session["resultado_primera"] * 0.40 + session["resultado_segunda"] * 0.60
            
            nota_acumulada = f"{acumulada:.1f}"


    return render_template("index.html",nota_final_primera=nota_final_primera,nota_final_segunda=nota_final_segunda,nota_acumulada=nota_acumulada)

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)