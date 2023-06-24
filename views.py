"""
This module contains the views/routes of the website.
"""

from flask import jsonify, request, session,redirect,url_for,render_template
from main import app
from assets import officials,inmates
import json


def search_in_database(name, dob, adhar, nationality, state, address, ipc, jailType, jailLocation, jailCount):
    # Perform the search and find the intersection in the database

    # Assuming you have a database table named 'records'
    # with columns corresponding to the fields being searched

    # Start with all records
    results = get_all_records()
    # Apply filters based on the provided search criteria
    if name:
        results = filter_records_by_name(results, name)
    if dob:
        results = filter_records_by_dob(results, dob)
    if adhar:
        results = filter_records_by_adhar(results, adhar)
    if nationality:
        results = filter_records_by_nationality(results, nationality)
    if state:
        results = filter_records_by_state(results, state)
    if address:
        results = filter_records_by_address(results, address)
    if ipc:
        results = filter_records_by_ipc(results, ipc)
    if jailType:
        results = filter_records_by_jail_type(results, jailType)
    if jailLocation:
        results = filter_records_by_jail_location(results, jailLocation)
    if jailCount:
        results = filter_records_by_jail_count(results, jailCount)

    return results

# Implement functions to filter records based on each field

def filter_records_by_name(records, name):
    return [record for record in records if record['name'] == name]

def filter_records_by_dob(records, dob):
    return [record for record in records if record['dob'] == dob]

def filter_records_by_adhar(records, adhar):
    return [record for record in records if record['adhar'] == adhar]

def filter_records_by_nationality(records, nationality):
    return [record for record in records if record['nationality'] == nationality]

def filter_records_by_state(records, state):
    return [record for record in records if record['state'] == state]

def filter_records_by_address(records, address):
    return [record for record in records if record['address'] == address]

def filter_records_by_ipc(records, ipc):
    return [record for record in records if record['ipc'] == ipc]

def filter_records_by_jail_type(records, jailType):
    return [record for record in records if record['jail_type'] == jailType]

def filter_records_by_jail_location(records, jailLocation):
    return [record for record in records if record['jail_location'] == jailLocation]

def filter_records_by_jail_count(records, jailCount):
    return [record for record in records if record['times_in_jail'] == jailCount]

# Function to get all records from the database
def get_all_records():
    # Retrieve all records from the database
    # ...
    # Replace this with your actual implementation to fetch records from the database
    # ...

    # Example records
    records=inmates.read_inmate()

    return records
@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    # Extract the data from the request
    name = data.get("name")
    dob = data.get("dob")
    adhar = data.get("adhar")
    nationality = data.get("nationality")
    state = data.get("state")
    address = data.get("address")
    ipc = data.get("ipc")
    jailType = data.get("jailType")
    jailLocation = data.get("jailLocation")
    jailCount = data.get("jailCount")

    # Perform the search and find the intersection in the database
    results = search_in_database(name, dob, adhar, nationality, state, address, ipc, jailType, jailLocation, jailCount)
    print(results)
    # Return the results as a response
    return jsonify(results)


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