from flask import Flask, Blueprint, render_template, request, session, url_for, redirect, flash

view = Blueprint("views", __name__)

# GLOBAL CONSTANTS

NAME_KEY = 'name'

# VIEWS

@view.route("/login", methods=["POST", "GET"])
def login():
    """displays main login page and handles saving name in the session"""
    if request.method == "POST":
        name = request.form.get("inputName")
        if len(name) >= 2:
            session[NAME_KEY] = name
            flash(f"You were successfully logged in as {name}.")
            return redirect(url_for("views.home"))
        else:
            flash(f"Your name must be longer than one character.")
    return render_template("login.html", **{"session": session})


@view.route("/", methods=["POST", "GET"])
@view.route("/home", methods=["POST", "GET"])
def home():
    """displays home page if logged in"""
    if NAME_KEY not in session:
        return redirect(url_for("views.login"))  
    return render_template("index.html", **{"session": session})

@view.route("/history")
def history():
    return render_template("history.html", **{"session": session})

@view.route('/logout')
def logout():
    session.pop(NAME_KEY, None)
    flash("You were logged out.")
    return redirect(url_for("views.login"))
