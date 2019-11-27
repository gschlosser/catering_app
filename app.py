# from flask import Flask, url_for, redirect, request
# from flask_sqlalchemy import SQLAlchemy
# from models import users, orders
# from models import db
# from controllers import autho_controller

# app = Flask(__name__)

# db.init_app(app)

# app.register_blueprint('autho_blueprint', prefix = '/auth')

# #TODO:
# #app.register_blueprint('')


# @app.route('/')
# def home():
#     pass


# if __name__ == '__main__':
#     app.run()

from flask import Flask
from controllers import jwt, autho_blueprint, order_controller
from flask_sqlalchemy import SQLAlchemy
from models import db
from services import bcrypt
from services.user_service import create_user

app = Flask(__name__)

#setting our config style
app.config.from_object('config.Development')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/blog_dev_dbs'

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


# from models.users import Users
# from models.orders import Orders


# from models.user import User

@app.route('/')
def say_hello(): 
    return 'hello!'

#import blueprint here
app.register_blueprint(autho_blueprint, url_prefix='/auth')
app.register_blueprint(order_controller, url_prefix='/order')
#Any other routes here

if __name__ == '__main__':
    app.run()