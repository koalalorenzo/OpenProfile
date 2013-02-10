from openprofile import app
from openprofile import db
from openprofile.decorators import *

from openprofile.objects import Page
from openprofile.objects import Profile

from random import choice

from flask import render_template
from flask import url_for
from flask import abort
from flask import redirect
from flask import flash

import markdown

@app.route('/installation/')
def installation_index():
    """Home page of the profile"""
    return render_template('installation/first_run.html')
