import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authn.serializers import authn_orgunit_request
from rest_api_demo.api.authn.parsers import orgunit_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import AuthnOrgUnit

log = logging.getLogger(__name__)

ns = api.namespace('authn/orgunits', description='Operations related to oganizational units within accounts')

@ns.route('/')
class OrgUnitsCollection(Resource):

    @api.expect(orgunit_request_arguments)
    @api.marshal_with(authn_orgunit_request)
    def get(self):
        """
        Returns OrgUnits
        """
        args = orgunit_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        return AuthnOrgUnit.query.filter(AuthnOrgUnit.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class OrgUnitItem(Resource):

    @api.marshal_with(authn_orgunit_request)
    def get(self, id):
        """
        Returns an orgunit
        """
        return AuthnOrgUnit.query.filter(AuthnOrgUnit.id == id).one()
