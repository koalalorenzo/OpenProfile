from openprofile import app
from openprofile.decorators import *

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/<page>")
def page(page):
    return "Hello World!"
