from models.category_model import CategoryMaster
from utils import serializer


class CategoryMasterSchema(serializer.ModelSchema):
    class Meta:
        model = CategoryMaster


categoryMasterSchema = CategoryMasterSchema()
categoriesMasterSchema = CategoryMasterSchema(many=True)
