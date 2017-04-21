# coding:utf-8

from flask import Flask,views
import flask
import config
from exts import db
from flask_wtf import CSRFProtect
from models import User
from forms import RegistForm,LoginForm
from auth import login_required
import constants


app = Flask(__name__)
app.debug = True
app.config.from_object(config)
db.init_app(app)
#CSRFProtect(app)


@app.route('/')
def index():
    return flask.render_template('index.html')

#注册视图函数
class RegistView(views.MethodView):

    def get(self):
        return flask.render_template('regist.html')

    def post(self):
        form = RegistForm(flask.request.form,csrf_enabled=False)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(email=email,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return flask.render_template('regist_success.html')
        else:
            print form.errors
            return u'注册失败'

#登陆视图函数
class LoginView(views.MethodView):

    def get(self):
        return flask.render_template('login.html')

    def post(self):
        form = LoginForm(flask.request.form,csrf_enabled=False)
        if form.validate():
            email = form.email.data
            remember = form.remember.data
            flask.session[constants.USER_SESSION_ID] = email
            if remember:
                flask.session.permanent = True
            return u'登陆成功'
        else:
            print form.errors
            return u'登陆失败'

#单单get方法
# @app.route('/transfer/')
# @login_required
# def transfer():
#     email = flask.request.args.get('email')
#     money = float(flask.request.args.get('money'))
#     user = User.query.filter_by(email=email).first()
#
#     myemail = flask.session.get(constants.USER_SESSION_ID)
#     myself = User.query.filter_by(email=myemail).first()
#
#     if myself.deposit > money:
#         myself.deposit -= money
#         user.deposit += money
#         db.session.commit()
#         return  u'转账成功'
#     else:
#         return u'你的余额不足'

@app.route('/transfer/',methods=['GET','POST'])
@login_required
def transfer():
    if flask.request.method == 'GET':
        return flask.render_template('transfer.html')
    else:
        email = flask.request.form.get('email')
        money = float(flask.request.form.get('money'))
        user = User.query.filter_by(email=email).first()

        myemail = flask.session.get(constants.USER_SESSION_ID)
        myself = User.query.filter_by(email=myemail).first()

        if myself.deposit > money:
            myself.deposit -= money
            user.deposit += money
            db.session.commit()
            return  u'转账成功'
        else:
            return u'你的余额不足'





app.add_url_rule('/regist/',view_func=RegistView.as_view('regist'))
app.add_url_rule('/login/',view_func=LoginView.as_view('login'))



if __name__ == '__main__':
    app.run(port=80)
