from flask_restplus import fields
from rest_api_demo.api.restplus import api

authn_role = api.model('Authenticated Role', {
    'id': fields.Integer(readonly=True, description='The unique identifier of a blog post'),
    'role_name': fields.String(required=True, description='Article title'),
})

authn_role_request = api.model('Authentication Role Request', {
    'user_id': fields.Integer(required=True, description='The id of the user'),
    'tenant_name': fields.String(required=True, description='The name of the medical practice'),
    'location_name': fields.String(required=False, description='The name of the location of the practice')
})




