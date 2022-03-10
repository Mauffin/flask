from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)

app.secret_key = "llave super secreta"#establecemos una clave secreta para dar mas seguridad alas cookies


#en nuestra ruta raiz quiero que se muestre un formulario
@app.route('/')
def formulario():
    return render_template('index.html')

#guardamos info en sesion

#usamos redirect para evitar 
@app.route('/procesado', methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['localizacion'] = request.form['localizacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentarios'] = request.form['comentarios']
    return redirect('/procesado')

@app.route('/procesado')
def success():
    return render_template('procesado.html')

if __name__ == "__main__":
    app.run(debug=True)