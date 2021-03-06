#! /usr/bin/env python

import os

from flask_script import Server, Manager

from project import create_app, db, bcrypt
from project.models.user import User


app = create_app(os.getenv('PROJECT_CONFIG', 'default'))


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def create_db():
    '''Creates the db tables.'''
    # db.drop_all()
    db.create_all()
    # db.session.add(User('root', bcrypt.generate_password_hash('root'), None))
    # db.session.commit()

@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()
    
if __name__ == '__main__':
    manager.run()
