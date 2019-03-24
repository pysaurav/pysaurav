#March 24, 2019
#Slarde

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/home')
def hello_world():
    return render_template("index.html")

@app.route('/techblog')
def tech():

    return render_template("/index.html")

@app.route('/thoughts')
def thoughts():
    return render_template("/index.html")

if __name__ == '__main__':

	app.run(debug=True)
