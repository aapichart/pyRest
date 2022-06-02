from flask import current_app
from sqlalchemy import create_engine
import json

# This class can solve problem regarding datetime column convert to json string, 
#   using in req_engine procedure
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

def req_engine(queryStr, params):
    #  This function return json string
    DBUri = current_app.config['DATABASE_URI']
    engine = create_engine(DBUri)
    with engine.connect() as conn:
        result = conn.execute(queryStr, params)
        s = json.dumps([dict(r) for r in result], cls=DatetimeEncoder)
    output = {'data': json.loads(s)}
    return output 
