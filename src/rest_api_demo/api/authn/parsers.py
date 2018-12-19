from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number', location='headers')
pagination_arguments.add_argument('bool', type=bool, required=False, default=1, help='Page number', location='headers')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                                  default=10, help='Results per page {error_msg}', location='headers')


role_request_arguments = reqparse.RequestParser()
role_request_arguments.add_argument('user-id', required=False, help='User Id', location='headers')
role_request_arguments.add_argument('practice-name', required=False, help='Name of the practice', location='headers')
role_request_arguments.add_argument('location-name', required=False, help='Location of the practice', location='headers')

