from flask import Blueprint 
from flask.templating import render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/signup')
def signUp():
    return render_template("signup.html")

