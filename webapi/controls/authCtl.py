from .globalTools import req_engine
from flask import current_app 
from flask import request
from flask import jsonify
from os import environ
from functools import wraps
import hashlib
import jwt 

# This function will decode Bearer token for payload inside, before getting into each end point
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = ''
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'Token is missing!'}) 
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_userid = data['id']
            current_username = data['username']
            current_iat = data['iat']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_userid, current_username, current_iat, *args, **kwargs)
    return decorated

def hashpassPrepare(inPassword):
    #  Using saltKey to encrypt by sha1 before saving or authenthicate each user
    saltKey = environ.get('SALT_KEY')
    inPassword = saltKey + inPassword
    inPassword = inPassword.encode('utf-8')
    hasspass = hashlib.sha1(inPassword).hexdigest()
    return hasspass


def queryCurrentUser(inId):
    # This function return json string
    s = req_engine("select id, username from users where id = %s", inId)
    return s

def queryUserByName(inUsername):
    #  This function return json string
    s = req_engine("select id, username, password from users where username = %s", inUsername)
    return s
