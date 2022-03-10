from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = "llavesecreta"


@app.route('/')
def index():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session['contador'] += 2
    return render_template("index.html")


@app.route('/destroy')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   