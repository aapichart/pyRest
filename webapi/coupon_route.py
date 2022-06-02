from .controls.couponCtl import queryCoupons 
from flask import Blueprint
from webapi.controls.authCtl import token_required

coupon_web_api = Blueprint('coupon_web_api', __name__)

@coupon_web_api.route('/coupons/<user_id>', methods=['GET'])
@token_required
def query_all_coupons(current_user, user_id):
    s = queryCoupons(user_id)
    return s 
