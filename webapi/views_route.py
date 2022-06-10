from flask_cors.decorator import cross_origin
from flask import Blueprint, request, make_response
from flask.json import jsonify
from flask import render_template
from flask_cors import cross_origin

from werkzeug.wrappers import response
from .models.users import Users
from webapi.controls.authCtl import queryUserByName, hashpassPrepare 
from flask_jwt_extended.utils import create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required

views_web_api = Blueprint('views_web_api', __name__)

@views_web_api.route('/dashboard', methods = ['GET'])
@cross_origin(origins='localhost',headers=['Content-Type','Authorization'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    response = jsonify({
            "login as " : current_user
        })
    return response 
