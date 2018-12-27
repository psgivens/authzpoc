import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authn.serializers import authn_user_request
from rest_api_demo.api.authn.parsers import pagination_arguments, user_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Post, AuthnUser

log = logging.getLogger(__name__)

ns = api.namespace('authn/users', description='Operations related to blog posts')


@ns.route('/')
class UsersCollection(Resource):

    @api.expect(user_request_arguments)
    @api.marshal_with(authn_user_request)
    def get(self):
        """
        Returns Users
        """
        args = user_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        return AuthnUser.query.filter(AuthnUser.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class UserItem(Resource):

    @api.marshal_with(authn_user_request)
    def get(self, id):
        """
        Returns a user
        """
        return AuthnUser.query.filter(AuthnUser.id == id).one()
