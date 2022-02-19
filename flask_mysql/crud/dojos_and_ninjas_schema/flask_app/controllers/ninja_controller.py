from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.all_dojos()
    return render_template("new_ninja.html", all_dojos = dojos)



@app.route("/new_ninjas", methods=["post"])
def add_ninja():
    data = {
        "dojo_id" : request.form["one_dojo.id"],
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : request.form["age"]
    }
    dojo_id = data["dojo_id"]
    Ninja.create_ninja(data)
    return redirect(f"/{dojo_id}")