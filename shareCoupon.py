from website import create_app 
from webapi import link_app

app = create_app()
app = link_app(app)

if __name__ == '__main__':
    app.run(debug=True)
