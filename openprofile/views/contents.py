from openprofile import app
from openprofile.decorators import *

@app.route('/')
def index():
    """Home page of the profile"""
    return 'Hello World!'

@app.route("/<page>")
def page(page):
    """Generic Page View"""
    return "Hello Page!"

@app.route("/avatar")
def avatar():
    """ Return the avatar """
    return "Hello World!"

@app.route("/card")
def vcard():
    """ Return the business card """
    return "Hello World!"

@app.route("/qrcode")
def qrcode():
    """ Return the qrcode to the profile """
    return "Hello World!"
