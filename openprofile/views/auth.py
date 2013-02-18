from openprofile import app 
from openprofile import db
from openprofile.decorators import *

from flask import render_template
from flask import session
from flask import redirect
from flask import flash
from flask import url_for

from openprofile.objects import Profile

@app.route("/auth/login", methods=['GET', 'POST'])
def login():
    next = request.args.get('next', '/admin', type=str)
    if 'auth' in session:
        return redirect(next)
        
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
        except KeyError:
            flash(u"Invalid Username or Password", "error")
            return render_template("auth/login.html", next=next)
            
        profile = Profile()
        profile.database = db
        profile.load_admin()
            
        if profile.verify_login(username, password):
            flash(u"Welcome back %s" % profile.username, "info" )
            session['auth'] = profile.userhash
            return redirect(next)
        else:
            flash(u"Invalid Username or Password", "error")
    return render_template("auth/login.html", next=next)
    
@app.route("/auth/logout")
def logout():
    if "auth" in session:
        flash("Goodbye!", "info") 
    session.pop('auth', None)
    return redirect(url_for('login'))
