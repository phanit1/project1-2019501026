import os
from flask import Flask, request, render_template
from models import *
from flask import Flask, session, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
engine = create_engine(os.getenv("DATABASE_URL"))

Session(app)
db.init_app(app)

@app.route('/')
def hello_world():
    return redirect('/register')
@app.route('/register', methods = ['POST','GET'])
def register():
    db.create_all()
    if request.method == 'POST':
        data = request.form
        userdata = USERS(request.form['email'],request.form['psw'])
        db.session.add(userdata)
        db.session.commit()
        return render_template("reg.html")
    else:
        return render_template("reg.html")