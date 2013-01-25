from flask import Flask, render_template, session, url_for, abort, redirect, flash, request

from pymongo import Connection, ASCENDING, DESCENDING
from configuration import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

db_connection =  Connection(MONGO_HOST, MONGO_PORT)
db = db_connection[MONGO_DB]
db.authenticate(MONGO_USERNAME,MONGO_PASSWORD)

# Static Files
@app.route('/static/<path:afilepath>')
def serve_static(afilepath):
    return redirect(url_for('static', filename=afilepath))

import openprofile.contents
import openprofile.admin
import openprofile.data
import openprofile.api
