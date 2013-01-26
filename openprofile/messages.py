from openprofile import app
from openprofile.decorators import *

@app.route("/messages/")
def conversations_list():
    return "Hello World!"

@app.route("/messages/<userhash>")
def conversation(userhash):
    """ See the conversation with another user."""
    return "Hello World!"

@app.route("/messages/send")
def send_message():
    """ Send the message to another OpenProfile."""
    return "Hello World!"

@app.route("/messages/receive", methods=['POST'])
def get_message():
    """ Receive the message from another OpenProfile."""
    return "Hello World!"

