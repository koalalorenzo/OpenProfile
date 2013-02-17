from openprofile import app
from openprofile.decorators import *
from openprofile.objects import Profile
import json

@app.route("/api/profile/owner")
def api_contact():
    """
        Returns the openprofile business card in json format: used by other installations
        it contains also the key (or a sort of ) to verify messages. If the key change,
        the owner must re-authorize the other friend.
    """
    profile = Profile()
    profile.load_admin()
    jsoned = profile.__dict__()
    del jsoned['is_admin']
    return json.dumps(jsoned)
