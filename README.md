## Es un programa que sería como una calculadora para saber las notas que uno tendría en el Q10 de la UPCA.

## Lo que hice al principio fue hacerlo sin Flask, normalito en Python.

<img width="585" height="381" alt="image" src="https://github.com/user-attachments/assets/03f441a7-42af-4c06-a959-7a85b5f23bae" />

Ahí se podía observar más o menos la idea que tenía, pero yo lo quería hacer para que se viera en la web y usé Flask, pero esta vez sí agregándole más detalles de lo que se observa en la imagen. 
Coloqué los dos cortes académicos del 40% y del 60%, una validación para que solo puedan ser números del 0 al 5 y agregué un botón para poder resetear al momento de ya haber ingresado las notas. 
También coloqué la posibilidad de solo hacer un corte a la vez.

¿Qué pasa? Por ejemplo, yo quiero saber cómo me quedaría el promedio del primer corte, así que separé los formularios porque en Flask explota si falta un dato, por eso es mejor hacer 
una separación de cada corte.

```python
if "nota1_primera" in request.form:

if "nota1_segunda" in request.form:
```

Ya con esa validación, Flask, si solo ve que se llenó el primer formulario, va a seguir funcionando normal y lo mismo si solo se llenó el segundo formulario.

Pero yo quería que se guardaran los resultados de cada corte. Por ejemplo, el primer corte salió que me quedó en 3.7 y, si yo ahora iba a calcular el segundo corte, 
se borraba lo que se había calculado en el primer corte porque es normal, se está haciendo un push. Pero no me servía porque lo que yo quería era que, si el usuario agregaba el primer corte y 
después el segundo, le saliera la nota acumulada de ambos cortes con sus porcentajes correspondientes: el primer corte 40% y el segundo 60%.

Así que usé:

```python
app.secret_key = "hola_profe"
```

para poder guardar los resultados en una `session`:

```python
session["resultado_primera"] = resultado_primera
session["resultado_segunda"] = resultado_segunda
```

Y cuando el programa detectara que el usuario calculó los dos cortes, se cumpliría esta condición:

```python
if "resultado_primera" in session and "resultado_segunda" in session:        
    acumulada = session["resultado_primera"] * 0.40 + session["resultado_segunda"] * 0.60
    nota_acumulada = f"{acumulada:.1f}"
```

Para poder calcular la nota acumulada y así quedó el programa. Está hecho a su estilo abstracto.

<img width="442" height="459" alt="image" src="https://github.com/user-attachments/assets/d153408a-8d9c-4796-8857-fca92891a36d" />
<img width="552" height="548" alt="image" src="https://github.com/user-attachments/assets/42fc9090-500d-41ee-a59c-a8e1877bda73" />

