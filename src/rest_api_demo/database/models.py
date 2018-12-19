# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_demo.database import db



class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80))

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return '<Role %r>' % self.role_name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, user_name, role):
        self.user_name = user_name
        self.role = role

    def __repr__(self):
        return '<User %r %r>' % self.user_name, self.role.role_name


class Context(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    practice_name = db.Column(db.String(80))
    location_name = db.Column(db.String(80))

    def __init__(self, practice_name, location_name):
        self.practice_name = practice_name
        self.location_name = location_name

    def __repr__(self):
        return '<Context %r %s>' % self.practice_name, self.location_name

class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(80))

    def __init__(self, feature_name):
        self.feature_name = feature_name

    def __repr__(self):
        return '<Feature %r>' % self.feature_name

class WebAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(80))
    resource_action = db.Column(db.String(8))

    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'))
    feature = db.relationship('Feature', backref=db.backref('web_actions', lazy='dynamic'))

    def __init__(self, resource_name, resource_action, feature):
        self.resource_name = resource_name
        self.resource_action = resource_action
        self.feature = feature
    
    def __repr__(self):
        return '<WebAction %r %r %r>' % self.resource_name, self.resource_action, self.feature.feature_name

















class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
