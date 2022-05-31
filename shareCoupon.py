from website import create_app 
from webapi import webapi_link_app

app = create_app()
app = webapi_link_app(app)

if __name__ == '__main__':
    app.run(debug=True)
