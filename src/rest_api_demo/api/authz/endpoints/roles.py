import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authz.serializers import authz_role
from rest_api_demo.api.authn.parsers import pagination_arguments, role_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import AuthzRole

log = logging.getLogger(__name__)

ns = api.namespace('authz/roles', description='Operations related to blog posts')


@ns.route('/')
class RolesCollection(Resource):

    @api.expect(role_request_arguments)
    @api.marshal_with(authz_role)
    def get(self):
        """
        Returns Roles
        """
        args = role_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        return AuthzRole.query.filter(AuthzRole.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class RoleItem(Resource):

    @api.marshal_with(authz_role)
    def get(self, id):
        """
        Returns a role
        """
        return AuthzRole.query.filter(AuthzRole.id == id).one()
