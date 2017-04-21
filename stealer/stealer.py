# coding:utf-8

from flask import Flask
import flask

app = Flask(__name__)
app.debug = True
app.config.update({
    'SERVER_NAME' : 'stealer.com:8000'
})



@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000)
