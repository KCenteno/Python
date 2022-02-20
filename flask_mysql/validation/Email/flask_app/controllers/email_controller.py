from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')


@app.route('/success')
def submit1():
    return render_template('success.html', emails = Email.get_all())

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    Email.delete(data)
    return redirect('/success')