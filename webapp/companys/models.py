from webapp import db
from datetime import datetime


class Company(db.Model):
    inn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240),index=True)
    directions = db.relationship("Direction",lazy='dynamic')
    def __repr__(self):
        return '<Company {}>'.format(self)

class Direction(db.Model):
    set_number = db.Column(db.Integer,primary_key=True)
    payer= db.Column(db.Integer,db.ForeignKey('company.inn'))#поменять местами с 25
    company_inn = db.Column(db.Integer,index=True,unique=True,)
    recipient = db.Column(db.Integer,index=True,unique=True)
    def __repr__(self):
        return '<Direction {}>'.format(self)
    
class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    type = db.Column(db.String(120), index=True)
    distanation = db.Column(db.String(240),index=True)
    summ = db.Column(db.Integer,index=True,unique=True)
    
    def __repr__(self):
        return '<Payments {}>'.format(self) 