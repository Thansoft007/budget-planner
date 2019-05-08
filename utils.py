from flask import url_for
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

orm = SQLAlchemy()
serializer = Marshmallow()


class FlaskApi(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)


class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


users = [
    User(1, 'thansoft', 'thansoft'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    print("authenticate called")
    return User(1, 'thansoft', 'thansoft')


def identity(payload):
    user_id = payload['identity']
    print("identity called")
    return userid_table.get(user_id, None)
