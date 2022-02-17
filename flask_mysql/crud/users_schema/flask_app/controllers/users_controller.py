from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.users import User

@app.route("/")
def all_users():
    users = User.all_users()
    return render_template("index.html", all_users = users)


@app.route("/new_user")
def new_user():
    return render_template("create.html")


@app.route("/<int:users_id>")
def show_user(users_id):
    data = {
        "id" : users_id
    }
    user = User.one_user(data)
    return render_template("show.html", one_user = user)

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save_user(data)
    return redirect("/")

@app.route("/delete/<int:users_id>")
def delete(users_id):
    data = {
        "id" : users_id
    }
    User.delete(data)
    return all_users()

@app.route("/edit/<int:users_id>")
def edit_user(users_id):
    data = {
        "id" : users_id
    }
    user = User.one_user(data)
    return render_template("edit.html", one_user = user)

@app.route("/update/<int:user_id>", methods=["POST"])
def edit(user_id):

    data = {
        "id" : user_id,
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    return all_users()

