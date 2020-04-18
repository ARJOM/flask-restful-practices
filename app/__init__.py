from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '90b3c011bfbbf4c746d967a0'
jwt = JWTManager(app)
api = Api(app)

from app import router