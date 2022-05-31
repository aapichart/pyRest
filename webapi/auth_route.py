from flask import Blueprint, request, current_app, make_response
from flask.json import jsonify
from flask.templating import render_template
from sqlalchemy import create_engine
import json
import hashlib
from os import environ
from .models.users import Users
import jwt
import datetime
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = queryCurrentUser(data['id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)

    return decorated

def hashpassPrepare(inPassword):
    #  Using saltKey to encrypt by sha1 before saving or authenthicate each user
    saltKey = environ.get('SALT_KEY')
    inPassword = saltKey + inPassword
    inPassword = inPassword.encode('utf-8')
    hasspass = hashlib.sha1(inPassword).hexdigest()
    return hasspass

def req_engine(queryStr, params):
    #  This function return json string
    DBUri = current_app.config['DATABASE_URI']
    engine = create_engine(DBUri)
    with engine.connect() as conn:
        result = conn.execute(queryStr, params)
        s = json.dumps([dict(r) for r in result])
    output = {'data': json.loads(s)}
    return output 

def queryCurrentUser(inId):
    # This function return json string
    s = req_engine("select id, username from users where id = %s", inId)
    return s

def queryUserByName(inUsername):
    #  This function return json string
    s = req_engine("select id, username, password from users where username = %s", inUsername)
    return s

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

