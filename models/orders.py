from . import db, users
from datetime import datetime

from marshmallow import Schema, fields

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    order = db.Column(db.String(300), nullable = False)
    address = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    date = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)
    
    def __init__(self, name, order, address, user_id, date, last_modified):
        self.name = name
        self.order = order
        self.address = address
        self.user_id = user_id
        self.date = date
        self.last_modified = last_modified

    def __repr__(self):
        return f'Thank you, {self.name}, your order for {self.order} will be delivered to {self.address} ASAP'

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_orders(id):
        return Orders.query.filter_by(user_id=id)




class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required = True)
    order = fields.Str(required = True)
    address = fields.Str(required = True)
    user_id = fields.Int(required=True)
    date_created = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime(dump_only=True)

