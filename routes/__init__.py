from utils import FlaskApi
from .category_route import category_ns

api = FlaskApi(version='1.0', title='Budget Planner', description='ThanSoft Budget Planner API',contact="8610930995",
               contact_email="thansoft.kb@gmail.com",authorizations={'Bearer Token': {"type": "apiKey", 'in': 'header', 'name': 'Authorization'}},security='Bearer Token')
api.add_namespace(category_ns)