import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authz.business import create_category, delete_category, update_category
from rest_api_demo.api.authz.parsers import features_request_arguments
from rest_api_demo.api.authz.serializers import authz_feature_request, category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category, AuthzFeature, Item

log = logging.getLogger(__name__)

ns = api.namespace('authz/features', description='Features that the user may be authorized to use.')


@ns.route('/')
class FeatureCollection(Resource):

    @api.expect(features_request_arguments)
    @api.marshal_list_with(authz_feature_request)
    def get(self):
        """
        Returns list of features available to the user
        """

        args = features_request_arguments.parse_args(request)
        user_id = args.get('user-id')
        account_id = args.get('account-id')
        org_unit_type = args.get('org-unit-type')
        org_unit_ids = args.get('org-unit-ids')

        return AuthzFeature.query.all()


@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class FeatureItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, id):
        """
        Returns a category with a list of posts.
        """
        return AuthzFeature.query.filter(AuthzFeature.id == id).one()

    @api.expect(category)
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
        update_authz_feature(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes blog category.
        """
        delete_authz_feature(id)
        return None, 204
