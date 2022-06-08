from os import wait
from flask import Blueprint, request, current_app, redirect, url_for
from flask import render_template 
from flask_jwt_extended.utils import get_jwt
from flask_jwt_extended.view_decorators import verify_jwt_in_request
import requests
from sqlalchemy.sql.elements import Null
from flask_cors import cross_origin
from webapi.controls.authCtl import token_required


auth = Blueprint('auth', __name__)


@auth.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Credentials']='True'
    header['Access-Control-Allow-Origin']='*'
    header['Access-Control-Allow-Headers']='Content-Type'
    header['Access-Control-Allow-Methods']='GET, POST'
    header['Access-Control-Allow-Credentials']=True
    return response

def req_webapi_url(endpoint):
    return "http://"+current_app.config['WEB_API_IP']+':'+current_app.config['WEB_API_PORT']+endpoint

@auth.route('/login', methods=['GET', 'POST'])
def login():
    messagestr = '' 
    if request.method == 'POST':
        loginData = request.form.get('login')
        passwordData = request.form.get('password')

        # in front of string symbols, u=unicode, b=byte, r=raw, f,F=format with litteral
        headers = {'Content-Type': 'application/json'}
        webapi_url = req_webapi_url('/api/login')
        response = requests.post(webapi_url, auth=(str(loginData), str(passwordData)), headers=headers)

        ### Start to redirect to dashboard endpoint
        # Authentication to webapi, if pass, show home page 
        # to show home page, we need to collect more information for homepage templates 
        if (response.status_code == 200):
            #  add token to headers before going into every end-points
        #  new_headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer '+token}
        #  print(new_headers)
            New_response = redirect(url_for("views.dashboard"))
            return New_response 
            #  return render_template("dashboard.html", token=token, headers=headers, user_is_authenticated=True) 
        #  else:
            #  messagestr = 'Incorrect Password!'
    return render_template("login.html", messagestr=messagestr, user_is_authenticated=False )

@auth.route('/logout', methods=['GET'])
@token_required
def logout(current_userid):
    headerstoken = request.headers.get('Authorization')
    print(headerstoken)
    if not current_userid == '':
        webapi_url = req_webapi_url('/api/logout')
        token = request.headers.get('Authorization')
        print(token)
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        resp = requests.get(webapi_url, headers=headers)
        output = resp.json()
        if output['token'] == '':
            return redirect(url_for('views.home')) 
    return redirect(url_for('views.home'))

@auth.route('/signup')
def signUp():
    return render_template("signup.html", user_is_authenticated=False)


