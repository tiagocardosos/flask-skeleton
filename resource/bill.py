from flask_restful import Resource


class Bill(Resource):
    def get(self, id):
        return {'id': id}

    def put(self, id):
        return {'put': {'id': id}}

    def delete(self, id):
        return {'delete': {'id': id}}


class BillList(Resource):
    def get(self):
        return {'data': []}

    def post(self):
        return {'post': {}}
