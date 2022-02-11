from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")



@app.route('/4')
def board4():
    return render_template("4.html")



@app.route('/multi/<int:num>')
def multi(num):
    return render_template('random.html', num = num)



if __name__=="__main__":
    app.run(debug=True)