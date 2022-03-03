from flask import Flask, render_template # importamos flask para permitirnos crear una aplicacion
app = Flask(__name__) #creando una instancia de flask y la llamo app

@app.route('/')
def hola_mundo():
    return "<h1>hola mundo!</h1>"

@app.route('/dojo')
def dojo():
    return"<h1>!Dojo!</h1>"

@app.route('/say/<nombre>')
def hola_nombre(nombre):
    return "Hola "+nombre


@app.route('/repeat/<int:num>/<string:palabra>')
def repite_palabra(num, palabra):
    output = ''
    for i in range(0, num):
        output += '<p>'+palabra+'</p>'
    return output 


if __name__ == "__main__": 
    app.run(debug=True)  