from flask import Blueprint, request, current_app, make_response
from flask.json import jsonify
from flask import render_template
import json
import hashlib
from .models.users import Users
from webapi.controls.authCtl import queryUserByName, hashpassPrepare, token_required
import jwt
import datetime


auth_web_api = Blueprint('auth_web_api', __name__)

@auth_web_api.route('/login')
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    s = queryUserByName(auth.username)
    if s['data'] == []:
        return jsonify({'message': "No User Found !! "}) 
    inId = s['data'][0]['id']
    inUsername = s['data'][0]['username']
    inPassword = s['data'][0]['password']
    hashpass = hashpassPrepare(auth.password)
    if hashpass == inPassword:
        #  if user is done authentication, we have to forward him to home pages by putting token in request headers
        tokenLife = current_app.config['TOKEN_TIMEOUT']
        token = jwt.encode({'id': inId,'username': inUsername, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=tokenLife)}, current_app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    return make_response("Password is incorrected!! ", 401, {'WWW-Authenticate': 'Basic realm="Login required!"'}) 

@auth_web_api.route('/logout')
@token_required
def logout(current_user):
    return render_template("logout.html", data=current_user)

@auth_web_api.route('/signup')
def signUp():
    return render_template("signup.html")

