from flask import Blueprint, json, request, jsonify
import json

users_web_api = Blueprint('users_web_api', __name__)

@users_web_api.route('/users', methods=['GET'])
def retrieve_users():
    outputData = {"message":[
                    {"username":"apichart", "score":"3.5", "addr":"139/1" },
                    {"username":"Krittinpong", "score":"3.5", "addr":"139/1"},
                    {"username":"Tasavapun", "score":"3.5", "addr":"139/1"},
                    {"username":"Pakintus", "score":"3.5", "addr":"139/1"},
                    {"username":"Tasavapun", "score":"3.5", "addr":"139/1"}
        ]}
    return jsonify(outputData)

@users_web_api.route('/users/<id>', methods=['GET'])
def logout():
    return "logout.html"

@users_web_api.route('/users/<id>', methods=['GET'])
def signUp():
    return "signup.html"
