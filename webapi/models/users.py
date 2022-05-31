from webapi import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usercode = db.Column(db.String[10], nullable=False)
    username = db.Column(db.String[20], nullable=False)
    password = db.Column(db.String[50], nullable=False)
    fullname = db.Column(db.String[80], nullable=False)
    datecreate = db.Column(db.DateTime, nullable=False)
    usercreate = db.Column(db.String[10])
    statususer = db.Column(db.Boolean)
    role_id = db.Column(db.Integer)
    email = db.Column(db.String[100])
    account_group_id = db.Column(db.Integer)
    member_id = db.Column(db.String[3])
    secret_code = db.Column(db.String[32])
    signature = db.Column(db.Text)
    signature_key = db.Column(db.String[30])
