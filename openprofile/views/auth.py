from openprofile import app 
from openprofile import db
from openprofile.decorators import *

from flask import render_template
from flask import session
from flask import redirect
from flask import flash

from openprofile.objects import Profile

@app.route("/auth/login", methods=['GET', 'POST'])
def login():
    if 'auth' in session:
        return render_template("auth/login.html")
        
    if request.method == 'POST':
        next = request.args.get('next', '')
        username = request.form['username']
        password = request.form['password']

        profile = Profile()
        profile.database = db
        profile.load_admin()
            
        if profile.verify_login(username, password):
            flash(u"Welcome back %s" % profile.username, "info" )
            session['auth'] = profile.userhash
            return redirect(next)
        else:
            flash(u"Invalid Username or Password", "error")
        return render_template("auth/login.html")
    return return render_template("auth/login.html")
    
@app.route("/auth/logout")
def logout():
    session.pop('auth', None)
    flash("Goodbye!", "info")    
    return render_template("auth/login.html")
