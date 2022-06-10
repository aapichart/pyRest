from flask_cors.decorator import cross_origin
from flask import Blueprint, request, make_response
from flask.json import jsonify
from flask import render_template
from flask_cors import cross_origin

from werkzeug.wrappers import response
from .models.users import Users
from webapi.controls.authCtl import queryUserByName, hashpassPrepare 
from flask_jwt_extended.utils import create_access_token, create_refresh_token, get_jwt_identity, set_access_cookies, set_refresh_cookies
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended.utils import unset_jwt_cookies

auth_web_api = Blueprint('auth_web_api', __name__)


@auth_web_api.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin']='*'
    header['Access-Control-Allow-Headers']='Content-Type'
    header['Access-Control-Allow-Methods']='GET, POST'
    header['Access-Control-Allow-Credentials']='True'
    return response

@auth_web_api.route('/login', methods=['POST'])
@cross_origin(origins='localhost',headers=['Content-Type','Authorization'])
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
    print(inUsername)
    hashpass = hashpassPrepare(auth.password)
    if hashpass == inPassword:
        #  if user is done authentication, we have to forward him to home pages by putting token in request headers
        additional_claims = {'username': inUsername}
        access_token = create_access_token(identity=inId, additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=inId, additional_claims=additional_claims)
        response = jsonify({"access_token": access_token})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    response = make_response({'message': "Password is incorrect!!", "token":""}, 401, {'WWW-Authenticate': 'Basic realm="Login required!"'}) 
    return response

@auth_web_api.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    current_userid = get_jwt_identity()
    response = jsonify({"msg": "logout sucessfully", "current_userid": current_userid})
    unset_jwt_cookies(response)
    return response 


@auth_web_api.route('/signup')
def signUp():
    return render_template("signup.html")

