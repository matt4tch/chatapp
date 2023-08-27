from flask import Flask, Blueprint, render_template, request, session, url_for, redirect

view = Blueprint("views", __name__)

# GLOBAL CONSTANTS

NAME_KEY = 'name'

# VIEWS

@view.route("/login", methods=["POST", "GET"])
def login():
    """displays main login page and handles saving name in the session"""
    if request.method == "POST":
        name = request.form["intputName"]


@view.route("/")
@view.route("/home")
def home():
    """displays home page if logged in"""
    if NAME_KEY not in session:
        return redirect(url_for("views.login"))
    return render_template("index.html", **{"session": session})