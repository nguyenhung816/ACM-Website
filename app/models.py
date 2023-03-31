from datetime import datetime
from app.database import db


#class User(db.Model):
   # created_at = db.Column(db.DateTime, default=datetime.utcnow)
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    member_number = db.Column(db.String(64), nullable=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    affiliation = db.Column(db.String(120), nullable=True)
    membership_type = db.Column(db.String(64), nullable=True)
    #date_added = db.Column(db.DateTime, default=datetime.utcnow().date().strftime('%Y-%m-%d'), nullable=True)
    date_added = db.Column(db.String(10), default=datetime.utcnow().strftime('%Y-%m-%d'), nullable=True)
    expiration_date = db.Column(db.DateTime, nullable=True)
    active_acm_member = db.Column(db.Boolean, nullable=True)
#main user account table ^^


class UserPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128))
    user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    email = db.Column(db.String(120), db.ForeignKey('user_account.email'), nullable=False)
#table with forbidden date x_x


    def __repr__(self):
        return '<UserPassword {}>'.format(self.email)