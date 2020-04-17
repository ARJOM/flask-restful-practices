from flask import request
from flask_restful import Resource, reqparse
from app.database.connection import get_db

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


class User(Resource):
    def get(self, user_id):
        cur = get_db().cursor()
        cur.execute(f"SELECT username FROM users WHERE id={user_id}")
        user = cur.fetchone()
        cur.close()

        return user

    def delete(self, user_id):
        cur = get_db().cursor()
        cur.execute(f"DELETE FROM users WHERE id={user_id}")
        get_db().commit()
        cur.close()

    def put(self, user_id):
        data = parser.parse_args()
        username = data['username']
        password = data['password']

        cur = get_db().cursor()
        cur.execute(f"UPDATE users SET username='{username}', password='{password}' WHERE id={user_id}")
        get_db().commit()
        cur.close()

        return 201


class UserList(Resource):
    def get(self):
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()

        return users

    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']

        cur = get_db().cursor()
        cur.execute(f"INSERT INTO users(username, password)"
                    f"VALUES ('{username}','{password}')")
        get_db().commit()
        cur.close()

        return 201
