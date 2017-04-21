# coding: utf-8
import os

DB_URL = 'mysql+mysqldb://root:123456@localhost:3306/icbc_demo?charset=utf8'

# SQLALCHEMY_DATABASE_URL = DB_URI

SQLALCHEMY_DATABASE_URI = DB_URL

# SECRET_kEY = os.urandom(24)
SECRET_KEY = os.urandom(24)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SERVER_NAME = 'icbc.com'