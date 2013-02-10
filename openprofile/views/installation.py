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

@app.route('/')
def installation_index():
    """Home page of the profile"""
    return render_template('homepage.html', html="ciao", profile=None)
