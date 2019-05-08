from flask_restplus import Namespace, Resource, fields
import jwt

# category list operations
authorization_ns = Namespace('authorization')





@authorization_ns.route('login/username/<string:username>/password/<string:password>')
class Authorization(Resource):

    @authorization_ns.doc('get bearer token')
    @authorization_ns.response(200, 'ok')
    @authorization_ns.response(201, 'created')
    def get(self, username, password):
        if (username == 'thansoft' and password == 'thansoft'):
            jwt.encode({},"thansoft_secret_key")
        else:
            return "invalid credentials", 200
