from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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
    newpw = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : newpw
    }
    Registration.save(data)
    reg_id = Registration.with_email(data)
    session["name"] = reg_id.first_name
    return redirect("/dashboard")


@app.route('/login', methods=["POST"])
def init():
    data = { "email" : request.form["email"] }
    user_in_db = Registration.with_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "log")
        return redirect('/')
    session['name'] = user_in_db.first_name
    return redirect("/dashboard")


@app.route('/reset')
def users_post():
    session.clear()
    return redirect('/')