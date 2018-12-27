import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authz.serializers import authz_account_request
from rest_api_demo.api.authz.parsers import account_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import AuthzAccount

log = logging.getLogger(__name__)

ns = api.namespace('authz/accounts', description='Operations related to defining accounts.')

@ns.route('/')
class AccountsCollection(Resource):

    @api.expect(account_request_arguments)
    @api.marshal_with(authz_account_request)
    def get(self):
        """
        Returns Accounts
        """
        args = account_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        return AuthzAccount.query.filter(AuthzAccount.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class AccountItem(Resource):

    @api.marshal_with(authz_account_request)
    def get(self, id):
        """
        Returns an account
        """
        return AuthzAccount.query.filter(AuthzAccount.id == id).one()
