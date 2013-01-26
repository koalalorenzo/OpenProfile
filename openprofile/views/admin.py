from openprofile import app
from openprofile.decorators import *
import json

@app.route("/admin/")
def admin_home():
    """Admin homepage view: the dashboard"""
    json.dumps({})
