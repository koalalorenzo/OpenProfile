#!/usr/bin/python
# -*- coding=utf-8 -*-

"""OpenProfile: Open your identity to the web"""

__version__ = "0.1"
__author__ = "Lorenzo Setale ( http://www.setale.me/ )"
__author_email__ = "koalalorenzo@gmail.com"
__license__ = "See: http://creativecommons.org/licenses/by-nd/3.0/ "
__copyright__ = "Copyright (c) 2009, 2010, 2011, 2012, 2013, 2014 Lorenzo Setale"

from flask import Flask
from flask import url_for
from flask import redirect

from pymongo import Connection
from configuration import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db_connection =  Connection(MONGO_HOST, MONGO_PORT)
db = db_connection[MONGO_DB]
db.authenticate(MONGO_USERNAME,MONGO_PASSWORD)

# Static Files
@app.route('/static/<path:afilepath>')
def serve_static(afilepath):
    return redirect(url_for('static', filename=afilepath))

import openprofile.views.auth
import openprofile.views.admin
import openprofile.views.api
import openprofile.views.contents
import openprofile.views.messages
import openprofile.views.installation

