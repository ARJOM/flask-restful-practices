from app import api
from app.controllers.user_controller import *

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:user_id>')
