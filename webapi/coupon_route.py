from .controls.couponCtl import queryCoupons 
from flask import Blueprint
from flask_jwt_extended.view_decorators import jwt_required 
from flask_jwt_extended import get_jwt_identity
from webapi.controls.authCtl import token_required

coupon_web_api = Blueprint('coupon_web_api', __name__)


@coupon_web_api.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin']='*'
    header['Access-Control-Allow-Headers']='Content-Type'
    header['Access-Control-Allow-Methods']='GET, POST'
    header['Access-Control-Allow-Credentials']=True
    return response

@coupon_web_api.route('/coupons/<user_id>', methods=['GET'])
@jwt_required()
def query_all_coupons():
    #  s is already json 
    s = queryCoupons(user_id)
    return s 
