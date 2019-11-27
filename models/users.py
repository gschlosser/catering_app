from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    # username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(500), nullable = False)
    # amount_of_orders = db.relationship('Orders', backref = 'author', lazy = True)

    def __init__(self, email, password):
        # self.username = username
        self.email = email
        self.password = password
        # self.amount_of_orders = amount_of_orders

    def __repr__(self):
        return f'Welcome, {self.email}!'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'user created'