from flask_restful import Resource, reqparse
from model.Tag import TagModel


class TagAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('active', default=True, type=bool)

    def get(self, id):
        tag = TagModel.query.get(id)
        if tag:
            return tag.json()

        return {"message": "ID '{}' not already exists.".format(id)}, 400

    def put(self, id):
        data = self.parser.parse_args()
        name = data['name']

        if TagModel.find_by_name(name):
            return {"message": "An tag with name '{}' already exists.".format(name)}, 400

        tag = TagModel(**data)
        try:
            tag.save_to_db()
        except:
            return {"message": "An error occurred insert the tag."}, 500

        return tag.json(), 201

    def delete(self, id):
        tag = TagModel.query.get(id)
        if tag:
            tag.delete_from_db()
            return {"message": "Tag deleted"}

        return {"message": "An error occurred delete the tag."}, 500


class TagListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('active', default=True, type=bool)

    def post(self):
        data = self.parser.parse_args()
        name = data['name']

        if TagModel.find_by_name(name):
            return {"message": "An tag with name '{}' already exists.".format(name)}, 400

        tag = TagModel(**data)
        try:
            tag.save_to_db()
        except:
            return {"message": "An error occurred insert the tag."}, 500

        return tag.json(), 201

    def get(self):
        tags = TagModel.query.all()

        return {"tags": [x.json() for x in tags]}
