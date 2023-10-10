from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()



class Brand(db.Model):
    brandid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    brand_name = db.Column(db.String(64),index=True,nullable=False)

class Product(db.Model):
    """the child class, parent is category"""
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    product_name = db.Column(db.String(64),index=True)
    product_price = db.Column(db.String(120))
    product_added_on = db.Column(db.DateTime(), default=datetime.utcnow)
    product_category = db.Column(db.Integer(), db.ForeignKey('category.catid'))
    product_brand = db.Column(db.Integer(), db.ForeignKey('brand.brandid'))
    # using the relationship
    catdeets = db.relationship("Category",back_populates="products")

class Category(db.Model):
    "parent class"
    catid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    catgory_name = db.Column(db.String(50),nullable=False)
    catgory_desc = db.Column(db.String(50),nullable=False)
      # using the relationship
    products = db.relationship("Product",back_populates="catdeets")


class Registration(db.Model):
    __tablename__="user_registration"
    regid = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    firsname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    pwd = db.Column(db.String(200), nullable=False)
    profile = db.Column(db.Text(), nullable=True)
    extra = db.Column(db.Text(), nullable=True)
    datereg = db.Column(db.DateTime(), default=datetime.utcnow)

    # def __repr__(self):
    #     return "<" + self.lastname + str(self.regid) + ">"


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    post_fullname = db.Column(db.String(60), nullable=False)
    post_content = db.Column(db.String(255), nullable=False)
    post_created_on = db.Column(db.DateTime(), default=datetime.utcnow)