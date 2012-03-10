#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 crackcell
#

from sheep.api.statics import static_files

#from flaskext.csrf import csrf
from flask import Flask

app = Flask(__name__)
app.debug = True
app.jinja_env.filters['s_files'] = static_files

#csrf(app)

from views import *
from models import *

