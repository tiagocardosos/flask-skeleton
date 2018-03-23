from flask_restful import Resource, reqparse
from model.Category import CategoryModel


class CategoryListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('type', required=True, choices=('A', 'D', 'C'), help='Type invalid! Ex: [A, D or C]')
        super(CategoryListAPI, self).__init__()

    def get(self):
        categories = CategoryModel.query.all()

        return {'categories': [x.json() for x in categories]}

    def post(self):
        data = self.parser.parse_args()
        category = CategoryModel(**data)

        try:
            category.save_to_bd()
        except:
            return {"message": "An error occurred insert the category."}, 500

        return category.json(), 201


class CategoryAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('type', required=True, choices=('A', 'D', 'C'), help='Type invalid! Ex: [A, D or C]')
        super(CategoryAPI, self).__init__()

    def get(self, id):
        category = CategoryModel.query.get(id)

        return category.json()

    def put(self, id):
        data = self.parser.parse_args()
        category = CategoryModel.query.get(id)
        category.name = data['name']
        category.type = data['type']

        try:
            category.update_to_bd()
        except:
            return {"message": "An error occurred update the category."}, 500

        return category.json(), 201

    def delete(self, id):
        category = CategoryModel.query.get(id)

        if category:
            category.delete_from_db()
            return {"message": "Category deleted"}

        return {"message": "An error occurred delete the category."}, 500


class CategoryTypeListAPI(Resource):
    def get(self, type):
        categories = CategoryModel.find_type(type)
        if categories:
            return {'categories': [x.json() for x in categories]}

        return {"message": "Type: '{}' not already exists.".format(type)}, 400
