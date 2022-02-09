from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hello(name):
    return f'Hi {name}!'

@app.route('/multi/<string:this>/<int:num>')
def multi(this, num):
    return f'Hi {this * num}!'


@app.route('/<path:u_path>')
def catch_all(u_path):
    return f'Sorry! {u_path} is not a defined path, Try again.'

if __name__=="__main__":
    app.run(debug=True)
