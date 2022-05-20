from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database 

def get_engine(user, passwd, host, port, dbname):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{dbname}"
    engine = create_engine(url)
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine
