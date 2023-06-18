"""
This module contains the views/routes of the website.
"""

from flask import jsonify, request, session,redirect,url_for
from main import app

user_data = (("Id", "username", "password"), ("id1", "ashish", "pass"))


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    for user in user_data[1:]:
        if user[0] == username and user[2] == password:
            session["user"]=username
            return {"message":"ok"},200

    return {"message":"Invalid Credentials"}, 400

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "user" in session:
        return "Logged in"
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.clear();
    return redirect(url_for("home"))