# Imports que son nativos del Framework y Librerias
from app import app

from flask import (
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
    flash,
)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/endpoints")
def endpoints():
    return render_template("endpoints.html")


@app.route("/models")
def models():
    return render_template("models.html")


@app.route("/manual")
def manual():
    return render_template("manual.html")
