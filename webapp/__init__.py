"""
Leon Santen
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # external help on how to work with sqlalchemy: minute 19 - https://www.youtube.com/watch?v=cYWiDiIUxQc&t=918s - from minute 18 - https://www.youtube.com/watch?v=44PvX0Yv368&t=562s
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fd5dd298e9002621b7e3c76bbf86372' #to get a random key: >>> python, >>> import secrets, >>> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webmix.db' # create database named "webmix.db"
db = SQLAlchemy(app) # create database instance
bcrypt = Bcrypt(app) # to hash passwords
login_manager = LoginManager(app)

from webapp import routes
