from utils import orm


class CategoryMaster(orm.Model):
    id = orm.Column(orm.Integer, primary_key=True)
    category = orm.Column(orm.String(100), nullable=False)
    createdDate = orm.Column(orm.DateTime, nullable=False)
    createdBy = orm.Column(orm.Integer, nullable=False)
