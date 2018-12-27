import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authn.serializers import authn_account_request
from rest_api_demo.api.authn.parsers import pagination_arguments, account_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import AuthnAccount

log = logging.getLogger(__name__)

ns = api.namespace('authn/accounts', description='Operations related to defining accounts.')

@ns.route('/')
class AccountsCollection(Resource):

    @api.expect(account_request_arguments)
    @api.marshal_with(authn_account_request)
    def get(self):
        """
        Returns Accounts
        """
        args = account_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        return AuthnAccount.query.filter(AuthnAccount.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class AccountItem(Resource):

    @api.marshal_with(authn_account_request)
    def get(self, id):
        """
        Returns an account
        """
        return AuthnAccount.query.filter(AuthnAccount.id == id).one()
