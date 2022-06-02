from .globalTools import req_engine

def queryCoupons(inUser):
    # This function return json string
    # {'data': ["":"", "":"", ..]}
    s = req_engine("select coupon_code, created_on, expired_on, campaign_id, hold_by, qrcode from coupons where hold_by = %s", inUser)
    return s
