from datetime import datetime
from app.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.relationship('UserPassword', backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class UserPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    def __repr__(self):
        return '<UserPassword {}>'.format(self.email)


#This defines a new User class with 
# five columns: id, first_name, last_name, email, password, 
# and created_at
