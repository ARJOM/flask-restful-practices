from flask_restful import Resource, reqparse
from app.database.connection import get_db
from app.utils import passwordEncrypt as pE
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


class Session(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {'logged_in_as': current_user}, 200

    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']

        password = pE.password_encrypt(password)

        cur = get_db().cursor()
        cur.execute(f"SELECT username FROM  users WHERE username='{username}' AND password='{password}'")
        user = cur.fetchone()
        cur.close()

        if user is None:
            return 401

        access_token = create_access_token(identity=username, )
        print(access_token)
        return {'access_token': access_token}, 200
