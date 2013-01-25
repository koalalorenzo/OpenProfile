from openprofile import app
from openprofile.decorators import *
import json

@app.route("/admin/")
def admin_home():
    # return the virtual business in json format
    json.dumps({})
