from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def start():
    return redirect("/dojos")


@app.route("/dojos")
def index():
    dojos = Dojo.all_dojos()
    return render_template("index.html", all_dojos = dojos)

@app.route("/<int:dojo_id>")
def show_dojo(dojo_id):
    data = {
        "id" : dojo_id
        
    }

    dojo = Dojo.one_dojo(data)
    ninja = Ninja.pick_one(data)
    return render_template("dojo_show.html", one_dojo = dojo, all_ninja = ninja)


@app.route("/new_dojo", methods=["post"])
def create_dojo():
    data = {
        "name" : request.form["name"] 
    }
    Dojo.add_dojo(data)
    return redirect("/")