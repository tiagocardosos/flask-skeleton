from run import api
from resource.bill import Bill, BillList
from resource.tag import TagAPI, TagListAPI
from resource.category import CategoryAPI, CategoryListAPI, CategoryTypeListAPI

api.add_resource(BillList, '/bill')
api.add_resource(Bill, '/bill/<int:id>')
api.add_resource(TagListAPI, '/tags', endpoint='tags')
api.add_resource(TagAPI, '/tag/<int:id>', endpoint='tag')
api.add_resource(CategoryAPI, '/category/<int:id>', endpoint='category')
api.add_resource(CategoryListAPI, '/categories', endpoint='categories')
api.add_resource(CategoryTypeListAPI, '/categories/type/<string:type>')
