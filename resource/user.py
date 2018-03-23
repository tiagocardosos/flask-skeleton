from flask_restful import Resource, reqparse
from middleware import jwt_required, current_identity
from model.User import UserModel


class UserLoggedAPI(Resource):
    @jwt_required()
    def get(self):
        return current_identity.json()


class UserRegisterAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('email', required=True, help='This field cannot be left blank!')
        self.parser.add_argument('password', required=True, help='This field cannot be left blank!')

    def post(self):
        data = self.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)

        try:
            user.save_to_bd()
        except:
            return {"message": "An error occurred insert the User."}, 500

        return user.json(), 201
