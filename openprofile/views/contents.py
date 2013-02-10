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
@cached()
def index():
    """Home page of the profile"""
    profile = Profile()
    profile.database = db
    profile.load_admin()
    page = Page("/")
    page.database = db
    try:
        page.load()
    except:
        abort(500)
    html = markdown.markdown(page.content)
    return render_template('homepage.html', html=html, profile=profile)

@app.route("/<page_url>")
@cached()
def page(page_url):
    """Generic Page View"""
    profile = Profile()
    profile.database = db
    profile.load_admin()
    
    page = Page("/%s" page_url)
    page.database = db
    try:
        page.load()
    except:
        abort(404)
    html = markdown.markdown(page.content)
    
    return render_template('page.html', page=page, html=html, profile=profile)

@app.route("/avatar")
def avatar():
    """ Return the avatar """
    return "Hello Avatar!"

@app.route("/card")
def vcard():
    """ Return the business card """
    return "Hello World!"

@app.route("/qrcode")
def qrcode():
    """ Return the qrcode that links the profile """
    return "Hello qrcode!"
