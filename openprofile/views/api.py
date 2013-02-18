from openprofile import app
from openprofile import db
from openprofile.decorators import *
from openprofile.objects import Profile
import json

@app.route("/api/profile")
@app.route("/api/profile/<userhash>")
def api_show_profile(userhash=None):
    """
        Returns the openprofile in json format: used by other installations
        it contains also the key (or a sort of ) to verify messages. If the key change,
        the owner must re-authorize the other friend.
    """
    profile = Profile()
    profile.database = db
    if not userhash:
        profile.load_admin()
    else:
        profile.userhash = userhash
        profile.load()
    jsoned = profile.__dict__()
    del jsoned['is_admin']
    return json.dumps(jsoned)
