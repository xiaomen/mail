#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 crackcell
#

from flask import Flask, render_template, redirect, \
    request, url_for, g

from mail import app
from mail.models import *

@app.route('/')
def index():
    return recv()

@app.route('/login')
def login():
    return redirect("http://account.xiaomen.co/?fr=mail.xiaomen.co")

@app.route('/recv')
def recv():
    if not g.user:
        return redirect(url_for('login'))
    uid = g.session['user_id']

    mails = Mail.get_recv_all(uid)
    return render_template('recv.html', mails = mails,
                           unread_mail_count =
                           Notification.get_unread_mail_count(uid))

@app.route('/sent')
def sent():
    if not g.user:
        return redirect(url_for('login'))
    uid = g.session['user_id']

    mails = Mail.get_sent_all(uid)
    return render_template('sent.html', mails = mails,
                           unread_mail_count =
                           Notification.get_unread_mail_count(uid))

@app.route('/view')
def view():
    if not g.user:
        return redirect(url_for('login'))
    uid = g.session['user_id']

    mid = request.args.get('id', '')
    mail = Mail.query.filter_by(id = mid).first()
    return render_template('view.html', mail = mail,
                           unread_mail_count =
                           Notification.get_unread_mail_count(uid))

@app.route('/write', methods=['GET', 'POST'])
def write():
    if not g.user:
        return redirect(url_for('login'))

    uid = g.session['user_id']
    to_uid = request.form.get('to_uid')
    if (request.method == 'GET'):
        return render_template('write.html',
                               unread_mail_count =
                               Notification.get_unread_mail_count(uid))

    Mail.insert(from_uid = uid,
                to_uid = to_uid,
                title = request.form.get('title'),
                content = request.form.get('content'))
    Notification.increase_unread(to_uid)
    return redirect('/')

