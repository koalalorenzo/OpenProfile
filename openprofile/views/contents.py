from openprofile import app
from openprofile.decorators import *
from random import choice

@app.route('/')
@cached()
def index():
    """Home page of the profile"""
    return 'Hello World!'

@app.route("/<page>")
@cached()
def page(page):
    """Generic Page View"""
    return "Hello Page! %s" % choice([0,1,2,3,4,5,6,7,8,9]) 

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
