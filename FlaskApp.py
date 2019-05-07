from flask import Flask
from flask_restplus import Api, Resource, fields
from os import environ
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields as ma_fields

app = Flask(__name__)
api = Api(app, version='1.0', title='POC API',
          description='A simple POC API',
          )

# app configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://4xBEJzOgUQ:thansoft105@remotemysql.com/4xBEJzOgUQ"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

category_ns = api.namespace('category', description='category in budget')


# category list operations
@category_ns.route('')
class CategoryList(Resource):

    @category_ns.doc('list categories')
    def get(self):
        return "testing"

    @category_ns.doc('create category')
    @category_ns.response(201, 'Created')
    def post(self):
        return "category created successfully", 201


# orm = SQLAlchemy(app)
# serializer = Marshmallow(app)


# # category master
# class CategoryMaster(orm.Model):
#     id = orm.Column(orm.Integer, primary_key=True)
#     category = orm.Column(orm.String(100), nullable=False)
#     createdDate = orm.Column(orm.DateTime, nullable=False)
#     createdBy = orm.Column(orm.Integer, nullable=False)
#
#
# class CategoryMasterSchema(serializer.ModelSchema):
#     class Meta:
#         model = CategoryMaster
#
#
# #  category master schema
# class CategorySchema(Schema):
#     id = ma_fields.Integer()
#     category = ma_fields.String()
#     createdDate = ma_fields.DateTime()
#     createdBy = ma_fields.Integer()
#
#
# # category_schema instance
# category_Schema = CategorySchema()
# categories_Schema = CategorySchema(many=True)
#
# categoryMasterSchema = CategoryMasterSchema()
#
# # category model
# category_ns = api.namespace('category', description='category in budget')
# category_model = api.model('category', {
#     'id': fields.Integer(description='category unique identifier'),
#     'category': fields.String(required=True, description='name of the category'),
#     'createdDate': fields.DateTime(dt_format='iso8601', description="category created date and time"),
#     'createdBy': fields.Integer(description='category created user')
# })
#
#
# # category list operations
# @category_ns.route('')
# class CategoryList(Resource):
#
#     @category_ns.doc('list categories')
#     @category_ns.response(200, 'ok')
#     @category_ns.marshal_list_with(category_model)
#     def get(self):
#         return categories_Schema.dump(CategoryMaster.query.all()).data
#
#     @category_ns.doc('create category')
#     @category_ns.response(201, 'Created')
#     @category_ns.expect(category_model)
#     def post(self):
#         category = categoryMasterSchema.load(api.payload).data
#         orm.session.add(category)
#         orm.session.commit()
#         return "category created successfully", 201
#

# @category_ns.route('/<int:cat_id>')
# @category_ns.param('cat_id', 'category id')
# class Category(Resource):
#     @category_ns.doc('create category')
#     @category_ns.response(201, 'created')
#     def get(self, cat_id):
#         return "getting category of id {0}".format(cat_id)
#
#     @category_ns.doc('create category')
#     @category_ns.response(201, 'Created')
#     def post(self, message):
#         return message

if __name__ == "__main__":
    # orm.create_all()
    app.run(debug=False, port=environ.get('PORT', 5000), host="0.0.0.0")
