from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "LoginPage"

@auth.route('/logout')
def logout():
    return "Log out Page"

@auth.route('/sign-up')
def signUp():
    return "sign-up Page"
