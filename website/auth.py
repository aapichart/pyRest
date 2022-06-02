from flask import Blueprint, request, current_app, redirect, url_for
from flask import render_template
import requests

from webapi.controls.authCtl import token_required


auth = Blueprint('auth', __name__)

def req_webapi_url(endpoint):
    return "http://"+current_app.config['WEB_API_IP']+':'+current_app.config['WEB_API_PORT']+endpoint

@auth.route('/login', methods=['GET', 'POST'])
def login():
    messagestr = '' 
    if request.method == 'POST':
        loginData = request.form.get('login')
        passwordData = request.form.get('password')

        headers = {'Content-Type': 'application/json'}
        webapi_url = req_webapi_url('/api/login')
        response = requests.get(webapi_url, auth=(loginData, passwordData), headers=headers)

        # Authentication to webapi, if pass, show home page 
        # to show home page, we need to collect more information for homepage templates 
        if response.status_code == 200:
            token = response.json()
            # add token to headers before going into every end-points
            hearders = {'Content-Type': 'application/json', 'x-access-token': token['token']}
            data = token
            return render_template("dashboard.html")
        messagestr = 'Incorrect Password!'
    return render_template("login.html", messagestr=messagestr)

@auth.route('/logout')
@token_required
def logout(current_user):

    return render_template("logout.html")

@auth.route('/signup')
def signUp():
    return render_template("signup.html")


