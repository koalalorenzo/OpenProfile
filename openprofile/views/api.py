from openprofile import app
from openprofile.decorators import *
import json

@app.route("/api/peers/contact")
def api_contact():
    """
        Returns the openprofile business card in json format: used by other installations
        it contains also the key (or a sort of ) to verify messages. If the key change,
        the owner must re-authorize the other friend.
    """
    return json.dumps({})