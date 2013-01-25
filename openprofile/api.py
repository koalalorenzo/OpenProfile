from openprofile import app
from openprofile.decorators import *
import json

@app.route("/api/peers/contact")
def api_contact():
    # return the openprofile business card in json format: used by other installations
    # it contains also the key (or a sort of ) to encrypt messages. if this key changes
    # the owner must re-authorize the other friend.
    json.dumps({})