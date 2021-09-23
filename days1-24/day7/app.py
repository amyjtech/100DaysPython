# Tech with Tem
# Make a Python Website as fast as possible

# Install flask module via 'pip3 install flask'

# Init flask
from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
