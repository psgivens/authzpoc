from rest_api_demo.database import db
from rest_api_demo.database.models import Post, Category

def create_role_request(data):
    title = data.get('user_id')
    body = data.get('tenant_name')
    category_id = data.get('location_name')
    category = Category.query.filter(Category.id == category_id).one()
    post = Post(title, body, category)



