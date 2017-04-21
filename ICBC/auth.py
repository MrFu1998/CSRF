# coding: utf-8
import flask
import constants
from models import User
from functools import  wraps

def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        email = flask.session.get(constants.USER_SESSION_ID)
        user = User.query.filter_by(email=email).first()
        if  email and user:
            return func(*args,**kwargs)
        else:
            return flask.redirect(flask.url_for('login'))
    return wrapper