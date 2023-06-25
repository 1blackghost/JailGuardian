"""
This module contains the views/routes of the website.
"""

from flask import jsonify, request, session, redirect, url_for, render_template
from main import app
from assets import officials, inmates
import json


def search_in_database(name, dob, adhar, nationality, state, address, ipc, jailType, jailLocation, jailCount):
    """
    Search the database for records that match the provided criteria.

    Args:
        name (str): Name of the inmate.
        dob (str): Date of birth of the inmate.
        adhar (str): Aadhar number of the inmate.
        nationality (str): Nationality of the inmate.
        state (str): State of the inmate.
        address (str): Address of the inmate.
        ipc (str): IPC section of the inmate.
        jailType (str): Type of jail the inmate has been to.
        jailLocation (str): Location of the jail the inmate has been to.
        jailCount (str): Number of times the inmate has been in jail.

    Returns:
        list: List of records matching the search criteria.
    """

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


def filter_records_by_name(records, name):
    """
    Filter the records by the given name.

    Args:
        records (list): List of inmate records.
        name (str): Name of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['name'] == name]


def filter_records_by_dob(records, dob):
    """
    Filter the records by the given date of birth.

    Args:
        records (list): List of inmate records.
        dob (str): Date of birth of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['dob'] == dob]


def filter_records_by_adhar(records, adhar):
    """
    Filter the records by the given Aadhar number.

    Args:
        records (list): List of inmate records.
        adhar (str): Aadhar number of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['adhar'] == adhar]


def filter_records_by_nationality(records, nationality):
    """
    Filter the records by the given nationality.

    Args:
        records (list): List of inmate records.
        nationality (str): Nationality of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['nationality'] == nationality]


def filter_records_by_state(records, state):
    """
    Filter the records by the given state.

    Args:
        records (list): List of inmate records.
        state (str): State of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['state'] == state]


def filter_records_by_address(records, address):
    """
    Filter the records by the given address.

    Args:
        records (list): List of inmate records.
        address (str): Address of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['address'] == address]


def filter_records_by_ipc(records, ipc):
    """
    Filter the records by the given IPC section.

    Args:
        records (list): List of inmate records.
        ipc (str): IPC section of the inmate.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['ipc'] == ipc]


def filter_records_by_jail_type(records, jailType):
    """
    Filter the records by the given jail type.

    Args:
        records (list): List of inmate records.
        jailType (str): Type of jail the inmate has been to.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['jail_type'] == jailType]


def filter_records_by_jail_location(records, jailLocation):
    """
    Filter the records by the given jail location.

    Args:
        records (list): List of inmate records.
        jailLocation (str): Location of the jail the inmate has been to.

    Returns:
        list: Filtered list of records.
    """

    return [record for record in records if record['jail_location'] == jailLocation]


def filter_records_by_jail_count(records, jailCount):
    """
    Filter the records by the given jail count.

    Args:
        records (list): List of inmate records.
        jailCount (str): Number of times the inmate has been in jail.

    Returns:
        list: Filtered list of records.
    """


def get_all_records():
    """
    Get all the inmate records from the database.

    Returns:
        list: List of all inmate records.
    """
    records = inmates.read_inmate()
    return records


@app.route("/search", methods=["POST"])
def search():
    """
    Perform a search in the database based on the provided criteria.

    Returns:
        json: List of records matching the search criteria.
    """
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

    # Return the results as a response
    return jsonify(results)


@app.route("/update", methods=["GET", "POST"])
def update():
    """
    Update an inmate's information in the database.

    Returns:
        json: Response message.
    """
    data = request.get_json()
    uid = data.get("uid")
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

    inmates.update_inmate(uid, name, dob, adhar, nationality, state, address, ipc_section, jail_type, jail_location, times_in_jail)

    return jsonify({"message": "Inmate added successfully"}), 200


@app.route("/add", methods=["POST"])
def add_inmate():
    """
    Add a new inmate to the database.

    Returns:
        json: Response message.
    """
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
    """
    Log in an official to the system.

    Returns:
        json: Response message.
    """
    data = request.get_json()
    user_data = officials.read_user()

    username = data.get("username")
    password = data.get("password")

    for user in user_data:
        print(user)
        if user[0] == username and user[2] == password:
            session["user"] = username
            return {"message": "ok"}, 200

    return {"message": "Invalid Credentials"}, 400


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    """
    Render the dashboard template.

    Returns:
        template: Dashboard template.
    """
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    """
    Log out the currently logged-in official.

    Returns:
        redirect: Redirects to the home page.
    """
    session.clear()
    return redirect(url_for("home"))
