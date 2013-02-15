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
    """Install OpenProfile"""
    return render_template('installation/first_run.html')

@app.route('/installation/profile')
def installation_create_profile():
    """Create the Profile"""
    return render_template('installation/create_profile.html')
    
@app.route('/installation/homepage')
def installation_create_homepage():
    """Create the homepage"""
    return render_template('installation/create_homepage.html')
    
@app.route('/installation/completed')
def installation_completed():
    """Check if everything is done and say it to the user"""
    return render_template('installation/completed.html')