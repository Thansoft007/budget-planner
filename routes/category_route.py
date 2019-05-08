from flask_restplus import Namespace, Resource, fields
from models.category_model import CategoryMaster, orm
from schemas.category_schema import categoriesMasterSchema, categoryMasterSchema
from flask_jwt import jwt_required

# category list operations
category_ns = Namespace('category')
category_model = category_ns.model('category', {
    'id': fields.Integer(description='category unique identifier'),
    'category': fields.String(required=True, description='name of the category'),
    'createdDate': fields.DateTime(dt_format='iso8601', description="category created date and time"),
    'createdBy': fields.Integer(description='category created user')
})


@category_ns.route('')
class CategoryList(Resource):

    @category_ns.doc('list categories')
    @category_ns.response(200, 'ok')
    @category_ns.marshal_list_with(category_model)
    @jwt_required()
    def get(self):
        return categoriesMasterSchema.dump(CategoryMaster.query.all()).data

    @category_ns.doc('create category')
    @category_ns.response(201, 'Created')
    @category_ns.expect(category_model, validate=True)
    @jwt_required()
    def post(self):
        category = categoryMasterSchema.load(category_ns.payload).data
        orm.session.add(category)
        orm.session.commit()
        return "category created successfully", 201


@category_ns.route('/<int:cat_id>')
@category_ns.param('cat_id', 'category id')
class Category(Resource):
    @category_ns.doc('get category')
    @category_ns.response(200, 'ok')
    @category_ns.marshal_with(category_model)
    def get(self, cat_id):
        data = CategoryMaster.query.get(cat_id)
        if data == None:
            return "Not found", 404
        else:
            return categoryMasterSchema.dump(CategoryMaster.query.get(cat_id)).data

    @category_ns.doc('create category')
    @category_ns.response(201, 'Created')
    @category_ns.expect(category_model)
    def put(self, cat_id):
        data = CategoryMaster.query.get(cat_id)
        if data == None:
            return "Not found", 404
        else:
            data["category"] = category_ns.payload["category"]
            data["createdDate"] = category_ns.payload["createdDate"]
            data["createdBy"] = category_ns.payload["createdBy"]
            orm.session.add(data)
            orm.session.commit()
            return "category created successfully", 201
