"""
This module contains the views/routes of the website.
"""

from flask import jsonify, request, session,redirect,url_for,render_template
from main import app
from assets import officials,inmates
import json


def search(search_term):
    results = []
    inmate_data = inmates.read_inmate()

    for inmate in inmate_data:
        for field, value in inmate.items():
            if isinstance(value, str) and search_term in value:
                results.append(inmate)
                break
            elif isinstance(value, int) and str(search_term) in str(value):
                results.append(inmate)
                break

    return results


@app.route("/update",methods=["GET","POST"])
def update():
    data = request.get_json()
    uid=data.get("uid")
    name = data.get("name")
    dob = data.get("dob")
    adhar = data.get("adhar")
    nationality = data.get("nationality")
    state = data.get("state")
    address = data.get("address")
    ipc_section = data.get("ipc")
    jail_type = data.get("jailType")
    jail_location = data.get("jailLocation")
    times_in_jail = data.get("jailCount")

    inmates.update_inmate(uid,name, dob, adhar, nationality, state, address, ipc_section, jail_type, jail_location, times_in_jail)

    return jsonify({"message": "Inmate added successfully"}), 200    

@app.route("/collect/<id>",methods=["GET","POST"])
def collect(id):
    data=inmates.read_inmate(str(id))
    return json.dumps(data),200

@app.route("/getData",methods=["GET","POST"])
def getData():
    search_term = request.form.get("searchQuery")
    data=search(search_term)
    return data


@app.route("/add", methods=["POST"])
def add_inmate():
    data = request.get_json()

    name = data.get("name")
    dob = data.get("dob")
    adhar = data.get("adhar")
    nationality = data.get("nationality")
    state = data.get("state")
    address = data.get("address")
    ipc_section = data.get("ipc")
    jail_type = data.get("jailType")
    jail_location = data.get("jailLocation")
    times_in_jail = data.get("jailCount")

    inmates.insert_inmate(name, dob, adhar, nationality, state, address, ipc_section, jail_type, jail_location, times_in_jail)

    return jsonify({"message": "Inmate added successfully"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user_data = officials.read_user()

    username = data.get("username")
    password = data.get("password")

    for user in user_data:
        print(user)
        if user[0] == username and user[2] == password:
            session["user"]=username
            return {"message":"ok"},200

    return {"message":"Invalid Credentials"}, 400

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "user" in session:
        return render_template("dashboard.html",user=session["user"])
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.clear();
    return redirect(url_for("home"))