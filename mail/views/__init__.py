#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 crackcell
#

from flask import Flask, render_template, redirect, \
    request
from mailbox import app
from mailbox.models import *

@app.route('/')
def index():
    return recv()

@app.route('/write', methods=['GET', 'POST'])
def write():
    if (request.method == 'GET'):
        return render_template('mail.html')
    title = request.form.get('title', None)
    content = request.form.get('content', None)
    return content

@app.route('/recv')
def recv():
    mails = Mail.query.filter_by(from_uid=1).all()
    return render_template('recv.html', mails=mails)

@app.route('/sent')
def sent():
    mails = Mail.query.filter_by(to_uid=1).all()
    return render_template('sent.html', mails=mails)

@app.route('/view')
def view():
    mid = request.args.get('id', '')
    mail = Mail.query.filter_by(id=mid).first()
    return render_template('view.html', mail=mail)

@app.route('/write')
def write():
    if (request.method == 'GET'):
        return render_template('write.html')
    mail = Mail(from_uid=1,
                to_uid = request.form.get('to_uid'),
                title = request.form.get('title'),
                content = request.form.get('content'),
                is_read = False)
    db.session.add(mail)
    db.session.commmit()
    return redirect('/')
