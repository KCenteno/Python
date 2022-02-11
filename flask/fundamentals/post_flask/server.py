from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key= 'i like pie'

@app.route('/')
def index():
    return render_template("index.html")


# Grab our information from our post 
@app.route('/users', methods=['POST'])
def users_post():
    # logic
    print('You just hit the submit button')
    
    # example of grabbing date from form
    # request.form['name_of_input']
    print(request.form['name'])
    print(request.form['email'])

    # Adding form data into session
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    
    print(session['name'])

    return redirect('/afterpost')

# After POST - // POST POST
@app.route('/afterpost')
def from_post():
    print('hitting the new route after submitting')
    return render_template('second.html', name = session['name'])








if __name__=="__main__":
    app.run(debug=True)