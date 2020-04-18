from app import api
from app.controllers.session_controller import *

api.add_resource(Session, '/login')
