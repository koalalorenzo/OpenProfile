from openprofile import app
from openprofile.decorators import *

@app.route("/avatar")
def avatar():
    # return Avatar image in base of a format
    return "Hello World!"

@app.route("/card")
def vcard():
    # return the virtual business card in base of the specified format 
    return "Hello World!"

@app.route("/qrcode")
def qrcode():
    # return a qrcode image ( jpeg or png ) with  
    return "Hello World!"
