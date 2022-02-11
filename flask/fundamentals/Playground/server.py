from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def hello_world():
    return render_template('index.html')



@app.route('/play/<int:x>')
def boxX(x):
    return render_template('index.html', times = x )



@app.route('/play/<int:x>/<string:color>')
def second(x, color):
    return render_template('index.html', times=x, color=color)



if __name__=="__main__":
    app.run(debug=True)