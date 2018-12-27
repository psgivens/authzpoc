import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authn.serializers import authn_role
from rest_api_demo.api.authn.parsers import role_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import AuthnRole

log = logging.getLogger(__name__)

ns = api.namespace('authn/roles', description='Operations related to blog posts')


@ns.route('/')
class RolesCollection(Resource):

    @api.expect(role_request_arguments)
    @api.marshal_with(authn_role)
    def get(self):
        """
        Returns Roles
        """
        args = role_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        account_id = args.get('account-id')
        r = AuthnRole('samplerole')
        rs = [r]

        return rs
        # return AuthnRole.query.filter(AuthnRole.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class RoleItem(Resource):

    @api.marshal_with(authn_role)
    def get(self, id):
        """
        Returns a role
        """
        return AuthnRole.query.filter(AuthnRole.id == id).one()
