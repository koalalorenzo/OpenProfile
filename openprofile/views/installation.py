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
from flask import request
from flask import jsonify

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

@app.route('/api/installation/profile/new')
def installation_api_create_profile():
    """Create the Profile via API"""
    username = request.args.get('username')
    password = request.args.get('password')
    profile = Profile()
    profile.database = db
    profile.is_admin = True
    profile.username = username
    profile.set_userhash(password)
    profile.save()
    return jsonify(done=True)
