from flask_restplus import fields
from rest_api_demo.api.restplus import api

authn_role = api.model('AuthnRole', {
    'id': fields.Integer(required=True, description='The id of the user'),
    'role_name': fields.String(required=True, description='The name of the role')
})

authn_account_request = api.model('Account', {
    'id': fields.Integer(readonly=True, description='The unique identifier of an account'),
    'account_name': fields.String(required=True, description='Account title'),
})

authn_orgunit_request = api.model('Organizational Unit', {
    'id': fields.Integer(readonly=True, description='The unique identifier of an orgunit'),
    'account_id': fields.Integer(required=True, description='Account associated with org unit'),
    'orgunit_name': fields.String(required=True, description='Organizational Unit title'),
})


authn_user_request = api.model('Authentication Role Request', {
    'user_id': fields.Integer(required=True, description='The id of the user'),
    'tenant_name': fields.String(required=True, description='The name of the medical practice'),
    'location_name': fields.String(required=False, description='The name of the location of the practice')
})




