from app import api
from app.controllers.user_controller import *

api.add_resource(HelloWorld, '/home')
