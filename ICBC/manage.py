# coding: utf-8

from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from icbc import app
import models
from exts import db

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()