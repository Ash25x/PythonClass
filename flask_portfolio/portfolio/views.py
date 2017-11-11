from flask import Flask, render_template, request, url_for
from . import app


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        return render_template('profile.html', name = name, message = message )
    else:
        return render_template("index.html")

@app.route("/profile", methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template("profile.html", name = name, message = message)

@app.route("/annoying")
def annoying():
    return render_template("annoying.html")
