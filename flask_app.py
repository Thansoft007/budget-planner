from flask import Flask, jsonify
from os import environ
from routes import api
from utils import orm, serializer, authenticate, identity
from flask_jwt import JWT

app = Flask(__name__)
# app configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://4xBEJzOgUQ:thansoft105@remotemysql.com/4xBEJzOgUQ"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = 86400

orm.init_app(app)
serializer.init_app(app)
api.init_app(app)
jwt = JWT(app, authenticate, identity)

def customized_error_handler(error):
    return jsonify({
        'message': error.description,
        'code': error.status_code
    }), error.status_code


jwt.jwt_error_handler()



if __name__ == "__main__":
    # orm.create_all()
    app.run(debug=False, port=environ.get('PORT', 5000), host="0.0.0.0")
