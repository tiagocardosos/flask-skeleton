from run import api
from resource.bill import BillResource

api.add_resource(BillResource, '/')
