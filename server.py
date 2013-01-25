from flask import Flask, render_template, session, url_for, abort, redirect, flash, request
from werkzeug.contrib.cache import FileSystemCache
import json
from bson.json_util import dumps as bsonDumps

from pymongo import Connection, ASCENDING, DESCENDING

from configuration import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

cache = FileSystemCache(cache_dir="cache")

db_connection =  Connection(MONGO_HOST, MONGO_PORT)
db = db_connection[MONGO_DB]
db.authenticate(MONGO_USERNAME,MONGO_PASSWORD)

# Decorators

def cached(timeout=5*60, key='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator


# Contents URL

@app.route("/")
@cached()
def homepage():
    return "Hello World!"

# General URL

@app.route("/avatar")
def homepage():
    # return Avatar image in base of a format
    return "Hello World!"

@app.route("/card")
def homepage():
    # return the virtual business card in base of the specified format 
    return "Hello World!"

@app.route("/qrcode")
def homepage():
    # return a qrcode image ( jpeg or png ) with  
    return "Hello World!"

# API 

@app.route("/api/contact")
def homepage():
    # return the virtual business  
    return "Hello World!"

if __name__ == "__main__":
    app.run()