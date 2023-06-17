"""
This module contains the views/routes of the website.
"""

from flask import jsonify, request, session
from main import app



@app.route("/jail", methods=["GET"])
def quiz_for_id():
    return "jail"
