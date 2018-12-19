from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_demo.database.models import Post, Category, Role, User, Context, Feature, WebAction
    db.drop_all()
    db.create_all()

    # Authentication 
    role_admin = Role('admin')
    role_user = Role('user')
    user_ara = User('ara', role_admin)
    user_eric = User('eric', role_admin)
    user_anar = User('anar', role_user)
    user_phillip = User('phillip', role_user)
    db.session.add(user_eric)
    db.session.add(user_ara)
    db.session.add(user_anar)
    db.session.add(user_phillip)

    # Context
    context_amersi_sm = Context('amersi', 'santa monica')
    context_amersi_ny = Context('amersi', 'new york')
    context_smith_sm = Context('smith', 'santa monica')
    db.session.add(context_amersi_sm)
    db.session.add(context_amersi_ny)
    db.session.add(context_smith_sm)

    # Features
    feature_blog_reader = Feature('Blog reader')
    feature_blog_publisher = Feature('Blog publisher')

    # web actions
    action_blog_get = WebAction('/api/blogs', 'GET', feature_blog_reader)
    action_blog_post = WebAction('/api/blogs', 'POST', feature_blog_publisher)
    action_blog_put = WebAction('/api/blogs', 'PUT', feature_blog_publisher)
    action_blog_delete = WebAction('/api/blogs', 'DELETE', feature_blog_publisher)

    db.session.add(action_blog_get)
    db.session.add(action_blog_post)
    db.session.add(action_blog_put)
    db.session.add(action_blog_delete)

    category = Category('somecategory')
    post = Post('somepost', 'somebody', category)
    db.session.add(post)
    db.session.commit()
