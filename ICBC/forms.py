# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,ValidationError
from wtforms.validators import Length,Email,EqualTo,InputRequired
from models import User

class RegistForm(FlaskForm):
    email = StringField(validators=[Email(),InputRequired()])
    username = StringField(validators=[InputRequired(),Length(2,20)])
    password = StringField(validators=[InputRequired(),Length(6,30)])
    password_repeat = StringField(validators=[EqualTo('password')])
    def validate_email(self,filed):
        email = filed.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError(u'该邮箱已经注册,不能重复注册!!!')

class LoginForm(FlaskForm):
    email = StringField(validators=[Email(), InputRequired()])
    password = StringField(validators=[InputRequired(), Length(6, 30)])
    remember = StringField()

    def validate(self):
        if not super(LoginForm,self).validate():
            return False

        email = self.email.data
        password = self.password.data

        user = User.query.filter_by(email=email,password=password).first()

        if not user:
            self.email.errors.append(u'邮箱或密码错误')
            return False
        return True