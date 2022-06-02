from flask import Blueprint, render_template 
import requests

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET'])
def home():
    return render_template("home.html")

@views.route('/users')
def users():
    data = requests.get('http://127.0.0.1:5000/users')
    data2in = [ 
                {"name": "Pakintas", "score": "3.5", "addr":"139/1"},
                {"name": "Tasavapun","score": "4.0", "addr":"139/1"}
            ]
    return render_template("home.html", data1=data.text, data2=data2in, data3={"science":"World"}, data4={"python":"wonderful"})
