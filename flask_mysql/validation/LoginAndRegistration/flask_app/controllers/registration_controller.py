from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.registration import Registration


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", session = session)


@app.route('/register', methods=["POST"])
def new():
    if not Registration.validate_registers(request.form):
        return redirect("/")
    Registration.save(request.form)
    session["first_name"] = request.form["first_name"]
    return redirect("/dashboard")


@app.route('/login', methods=["POST"])
def init():
    if Registration.check_login(request.form):
        data = {
            'email' : request.form["email"]
        }
        user = Registration.with_email(data)
        session["first_name"] = user.first_name
        return redirect('/dashboard')
    else: 
        return  redirect('/')


@app.route('/reset')
def users_post():
    session.clear()
    return redirect('/')