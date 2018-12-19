import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.authn.business import create_blog_post, update_post, delete_post
from rest_api_demo.api.authn.serializers import authn_role_request, authn_role, blog_post, page_of_blog_posts
from rest_api_demo.api.authn.parsers import pagination_arguments, role_request_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Post, Role

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
        practice_name = args.get('practice-name')
        location_name = args.get('location-name')

        # posts_query = Role.query
        # posts_page = posts_query.paginate(1, 10, error_out=False)

        return Role.query.filter(Role.id == user_id).one()

    # @api.expect(authn_role_request)
    # @api.marshal_with(authn_role)
    # def post(self):
    #     """
    #     Creates a new blog post.
    #     """
    #     create_blog_post(request.json)
    #     return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class RoleItem(Resource):

    @api.marshal_with(authn_role)
    def get(self, id):
        """
        Returns a role
        """
        return Role.query.filter(Role.id == id).one()

    # @api.expect(blog_post)
    # @api.response(204, 'Post successfully updated.')
    # def put(self, id):
    #     """
    #     Updates a blog post.
    #     """
    #     data = request.json
    #     update_post(id, data)
    #     return None, 204

    # @api.response(204, 'Post successfully deleted.')
    # def delete(self, id):
    #     """
    #     Deletes blog post.
    #     """
    #     delete_post(id)
    #     return None, 204


# @ns.route('/archive/<int:year>/')
# @ns.route('/archive/<int:year>/<int:month>/')
# @ns.route('/archive/<int:year>/<int:month>/<int:day>/')
# class PostsArchiveCollection(Resource):

#     @api.expect(pagination_arguments, validate=True)
#     @api.marshal_with(page_of_blog_posts)
#     def get(self, year, month=None, day=None):
#         """
#         Returns list of blog posts from a specified time period.
#         """
#         args = pagination_arguments.parse_args(request)
#         page = args.get('page', 1)
#         per_page = args.get('per_page', 10)

#         start_month = month if month else 1
#         end_month = month if month else 12
#         start_day = day if day else 1
#         end_day = day + 1 if day else 31
#         start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
#         end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
#         posts_query = Post.query.filter(Post.pub_date >= start_date).filter(Post.pub_date <= end_date)

#         posts_page = posts_query.paginate(page, per_page, error_out=False)

#         return posts_page
