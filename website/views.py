from os import wait
from flask import Blueprint, blueprints, render_template, jsonify, request
from flask.helpers import make_response 
import requests
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.sql.functions import current_user

views = Blueprint('views', __name__)

@views.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Credentials']='True'
    header['Access-Control-Allow-Origin']='*'
    header['Access-Control-Allow-Headers']='Content-Type'
    header['Access-Control-Allow-Methods']='GET, POST'
    return response

@views.route('/', methods = ['GET'])
def home():
    return render_template("home.html", user_is_authenticated=False)

@views.route('/dashboard', methods = ['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    response = jsonify({
            "login as " : current_user
        })
    return response 

@views.route('/users')
def users():
    data = requests.get('http://127.0.0.1:5000/users')
    data2in = [ 
                {"name": "Pakintas", "score": "3.5", "addr":"139/1"},
                {"name": "Tasavapun","score": "4.0", "addr":"139/1"}
            ]
    return render_template("dashboard.html", data1=data.text, data2=data2in, data3={"science":"World"}, data4={"python":"wonderful"})
