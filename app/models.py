from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Instantiate the database
db = SQLAlchemy()

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),nullable = False,unique=True)
    password = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime,nullable = False, default=datetime.utcnow())

    cart_items = db.relationship("Carts",foreign_keys='Carts.user_id',back_populates="user")

    def __init__(self, email, password, first_name,last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()



class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable = False, unique=True)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(500), nullable = False)
    image_url = db.Column(db.String)

    associated_carts = db.relationship("Carts",foreign_keys='Carts.product_id',back_populates="product")

    def __init__(self, product_name, price, description, image_url):
        self.product_name = product_name
        self.price = price
        self.description = description
        self.image_url = image_url

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
    
class Carts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_quantity = db.Column(db.Integer,nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id),nullable=False)
    user = db.relationship("Users",back_populates="cart_items",foreign_keys=[user_id])
    
    product_id = db.Column(db.Integer, db.ForeignKey(Products.id),nullable=False)
    product = db.relationship("Products",back_populates="associated_carts",foreign_keys=[product_id])
    
    def __init__(self, user_id, product_id, item_quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.item_quantity = item_quantity

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
    
    
