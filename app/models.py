import datetime
from app import db, login_manager
from flask.ext.login import UserMixin
from app.utils import hash_password, verify_password


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    realname = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = password = db.Column(db.LargeBinary())
    events = db.relationship('Event', backref='author', lazy='dynamic')

    # TODO: Fix it.
    #date_created  = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #date_modified = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, username, password, realname, email):
        self.username = username
        self.password = hash_password(password)
        self.realname = realname
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    begin = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # TODO: Fix it.
    #date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
    #                                       onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<Event %r>' % (self.body)
