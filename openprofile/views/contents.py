from openprofile import app
from openprofile.decorators import *

from openprofile.objects import Page
from openprofile.objects import Profile

from random import choice

from flask import Flask, render_template, session, url_for, abort, redirect, flash, request

import markdown

@app.route('/')
def index():
    """Home page of the profile"""
    return 'Hello World!'

@app.route("/<page_url>")
def page(page_url):
    """Generic Page View"""
    profile = Profile()
    profile.load_admin()
    
    page = Page("/%s" page_url)
    page.load()
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
    """ Return the qrcode to the profile """
    return "Hello qrcode!"
