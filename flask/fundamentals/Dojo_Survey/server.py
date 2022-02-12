from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key= 'this is a secret'



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['Location'] = request.form['Location']
    session['Language'] = request.form['Language']
    session['Comment'] = request.form['Comment']
    return redirect('submit')


@app.route('/submit')
def submit1():
    return render_template('submit.html', name = session['name'], Location  = session['Location'], Language = session['Language'], Comment = session['Comment'])





if __name__=="__main__":
    app.run(debug=True)