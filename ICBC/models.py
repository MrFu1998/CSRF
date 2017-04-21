# coding: utf-8
from exts import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(50),unique=True,nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    deposit = db.Column(db.Float,default=0)

# class Article(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(100),nullable=True)
#     context = db.Column(db.Text,nullable=True)
#     pub_time = db.Column(db.DateTime,default=datetime.now())





