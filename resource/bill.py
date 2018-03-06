from flask_restful import Resource


class BillResource(Resource):
    def get(self):
        return {'hello': 'world'}
