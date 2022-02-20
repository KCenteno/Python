from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    if Survey.validate_survey(request.form):
        Survey.save(request.form)
        return redirect('/submit')
    return redirect('/')



@app.route('/submit')
def submit1():
    return render_template('submit.html', survey = Survey.get_last())