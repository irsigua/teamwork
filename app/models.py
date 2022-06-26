from app import db
from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 


class company_base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name_payer = db.Column(db.String(240),index=True)
    company_name_recipient = db.Column(db.String(240),index=True)
    
    def __repr__(self):
        return '<Company_base {}>'.format(self)

class inn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payer_inn = db.Column(db.Integer,index=True,unique=True)
    recipient_inn = db.Column(db.Integer,index=True,unique=True)
    def __repr__(self):
        return '<Inn {}>'.format(self)
    
class payment_base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    payment_type = db.Column(db.String(120), index=True)
    payment_distanation = db.Column(db.String(240),index=True)
    payment_summ = db.Column(db.Integer,index=True,unique=True)
    
    def __repr__(self):
        return '<Payment_base {}>'.format(self) 