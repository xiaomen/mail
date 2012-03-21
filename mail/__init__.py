#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 crackcell
#

from sheep.api.statics import static_files
from sheep.api.sessions import SessionMiddleware, FilesystemSessionStore
from flask import Flask, g

app = Flask(__name__)
app.debug = True
app.jinja_env.filters['s_files'] = static_files

app.wsgi_app = SessionMiddleware(app.wsgi_app, \
        FilesystemSessionStore(), \
        cookie_name="xid", cookie_path='/', \
        cookie_domain=".xiaomen.co")

@app.before_request
def before_request():
    g.session = request.environ['xiaomen.session']
    g.user = 'user_id' in g.session and g.session['user_id']
    g.session['user_id'] = 1
    uid = g.session['user_id']
    g.session['unread_mail_count'] = Mail.query.filter_by(to_uid=uid, is_read=0).count()

from views import *
from models import *
