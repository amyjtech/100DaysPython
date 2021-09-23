from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    # The name variable will render on the homepage
    return render_template("index.html", name="Stella")

# If you want the username to be a variable you use < >


# URL parameters
'''@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)'''

# QUERY parameters


@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html")

# return JSON


@views.route("/json")
def get_json():
    return jsonify({'name': 'Stella', 'type': 'Dog'})


# get data
'''def get_data():
    data = request.json
    return jsonify(data)'''

# Reroute


@views.route("/reroute")
def go_json():
    return redirect(url_for("views.get_json"))
