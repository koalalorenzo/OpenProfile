from openprofile import app
from openprofile.decorators import *
import json

@app.route("/api/contact")
def api_contact():
    # return the virtual business in json format
    json.dumps({})
