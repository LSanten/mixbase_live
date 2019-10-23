"""
Leon Santen

These are the methods of the webmix database as a part of the package in webapp_run.py
"""
from datetime import datetime
from webapp import db, login_manager
from flask_login import UserMixin #UserMixin is class that checks user for us

# Athentication of user when log in
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pair_posts = db.relationship('Pair', backref='author', lazy=True) #this is a releationship not a column -- backreference to Pair. You can find out author of a pair post by using pair.author #lazy=True --> sqlalchemy will load data directly when used
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"User('{self.username}', '{self.id}')"

class Pair(db.Model): #data table for transition pair
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    secondname = db.Column(db.String(30), nullable=True)
    firstartist = db.Column(db.String(30), nullable=False)
    secondartist = db.Column(db.String(30), nullable=True)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=1) ## TODO: change nullable back to False when login works
    guestname = db.Column(db.String(30), nullable=True)
    firstgenre = db.Column(db.String(30), nullable=True)
    secondgenre = db.Column(db.String(30), nullable=True)
    tags = db.Column(db.Text)
    difficulty = db.Column(db.Integer, nullable=True)

    #create getter and setter function for creating list that refers to children of transition
    #http://frankvalcarcel.com/blog/conveniently-storing-lists-in-database/
    _children = db.Column(db.String, default='0')
    @property
    def children(self):
        return [int(x) for x in self._children.split(';')]
    @children.setter
    def children(self, value):
        self._children += ';%s' % value

    def __repr__(self):
        return f"Pair('{self.firstname}', '{self.secondname}', '{self.date_posted}' )"
