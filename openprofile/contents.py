from openprofile import app
from openprofile.decorators import *

@app.route('/')
@cached()
def index():
    return 'Hello World!'

@app.route("/<page>")
@cached()
def page(page):
    return "Hello World!"
