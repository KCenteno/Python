from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key= 'i have alot of pets'


@app.route('/')
def index():
    if 'clicker' not in session:
        session['clicker'] = 0
    else:
        session['clicker'] += 1
    return render_template('index.html')


@app.route('/reset')
def users_post():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
