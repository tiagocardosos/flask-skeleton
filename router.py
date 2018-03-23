from app import app
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resource.bill import Bill, BillList
from resource.tag import TagAPI, TagListAPI
from resource.category import CategoryAPI, CategoryListAPI, CategoryTypeListAPI
from resource.user import UserLoggedAPI, UserRegisterAPI

jwt = JWT(app, authenticate, identity)
api = Api(app)

api.add_resource(BillList, '/bill')
api.add_resource(Bill, '/bill/<int:id>')
api.add_resource(TagListAPI, '/tags', endpoint='tags')
api.add_resource(TagAPI, '/tag/<int:id>', endpoint='tag')
api.add_resource(TagAPI, '/tag')
api.add_resource(CategoryAPI, '/category/<int:id>', endpoint='category')
api.add_resource(CategoryListAPI, '/categories', endpoint='categories')
api.add_resource(CategoryTypeListAPI, '/categories/type/<string:type>')
api.add_resource(UserLoggedAPI, '/logged')
api.add_resource(UserRegisterAPI, '/register')
