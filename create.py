import os

from flask import Flask, request, render_template,url_for
from models import *
from books import *
from flask import Flask, session, redirect
from flask_session import Session
from sqlalchemy import create_engine, desc , or_
from sqlalchemy.orm import scoped_session, sessionmaker
import logging

logging.basicConfig(level=logging.DEBUG)

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
    return redirect('/registration')
@app.route('/registration', methods = ['POST','GET'])
def register():
    db.create_all()
    if request.method == 'POST':
        userdata = USERS(request.form['email'],request.form['psw'])
        user = USERS.query.filter_by(emailid=request.form['email']).first()
        if user is not None:
            print("User is already existing. Please try to register with a new")
            var1 = "Error: User is already existing. Please try to register with a new one"
            return render_template("reg.html", var1 = var1)
        db.session.add(userdata)
        db.session.commit()
        print("Registration Success")
        var1 ='Registration Success'
        return render_template("reg.html", var1 = var1)
    else:
        return render_template("reg.html")
    

@app.route('/admin')
def admin():
    data = USERS.query.order_by(desc(USERS.timestamp)).all()
    return render_template("admin.html",admin = data)

@app.route('/auth', methods=['POST'])
def login():
    print(request.form)
    user = USERS.query.filter_by(emailid=request.form['email']).first()
    if user is not None:
        if bcrypt.verify(request.form['psw'], user.password):
            session['email'] = request.form['email']
            print(session)
            return redirect('/home')
        else:
            var1 = "Wrong Credentials"
            return render_template("reg.html", var1 = var1)
    else:
        print("You are not a registered user. Please first register to login")
        var1 = "Error: You are not a registered user. Please first register to login"
        return render_template("reg.html", var1 = var1)
@app.route('/home', methods=['POST','GET'])
def home():
    try:
        user=session['email']
        if request.method == 'POST':
            req  = request.form['search']
            reqs = str(req)
            bookss = dbscope.query(Books.isbn, Books.title, Books.author, Books.year).filter(or_(Books.title.like("%"+reqs+"%"), Books.author.like("%"+reqs+"%"), Books.isbn.like("%"+reqs+"%"))).all()
            if bookss.__len__()==0:
                var1 = "No search found"
                return render_template("login.html", var1 = var1, user = user)
            return render_template("login.html",bookss = bookss,formaction = '/home', user = user)
        return render_template("login.html", user = user)
    except Exception as e:
        print(e)
        var1 = "You must log in to view the homepage"
        return render_template("reg.html",var1 = var1)

@app.route('/logout')
def logout():
    try:
        session.clear()
        var1 = "Logged Out"
        return render_template("reg.html", var1 = var1)
    except:
        var1 = "You must first log in to logout"
        return render_template("reg.html",var1 = var1)
