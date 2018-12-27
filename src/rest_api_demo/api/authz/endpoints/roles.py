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

        return AuthzRole.query.filter(AuthzRole.id == user_id).one()

@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class RoleItem(Resource):

    @api.marshal_with(authz_role)
    def get(self, id):
        """
        Returns a role
        """

        account_id = args.get('account-id')

        #role has features
        return AuthzRole.query.filter(AuthzRole.id == id).one()


    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates a blog category.

        Use this method to change the name of a blog category.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Category Name"
        }
        ```

        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_role(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes blog category.
        """
        delete_role(id)
        return None, 204