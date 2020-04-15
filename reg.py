from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'
@app.route('/registration')
def hello():
    return render_template("reg.html")

if __name__ == '__main__':
   app.run(debug = True)