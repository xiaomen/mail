#!/usr/bin/env python
# -*- encoding: utf-8; indent-tabs-mode: nil -*-
#
# Copyright 2012 crackcell
#

from flaskext.sqlalchemy import SQLAlchemy
from mailbox import app
from mailbox.config import *

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

def init_db(app):
    db.init_app(app)
    db.app = app
    db.create_all()

class Mail(db.Model):
    __tablename__ = 'mail'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    from_uid = db.Column(db.Integer)
    to_uid = db.Column(db.Integer)
    title = db.Column(db.String(45))
    content = db.Column(db.Text)
    is_read = db.Column(db.Boolean)

    def __init__(self, from_uid, to_uid, title, content, is_read, *args, **kwargs):
        self.from_uid = from_uid
        self.to_uid = to_uid
        self.title = title
        self.content = content
        self.is_read = is_read
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
