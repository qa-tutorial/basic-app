from application import app
from flask import render_template, redirect, url_for, request
import requests
from os import getenv

# Route to home page
@app.route('/', methods = ["GET"])
def home():
    response = requests.get("https://l5iqv5z489.execute-api.eu-west-2.amazonaws.com/test/get-name")
    package = response.json()
    name = f"{package['firstname']} {package['surname']}"
    machine = getenv("HOSTNAME")
    return render_template('index.html', title = 'Home', name = name, machine = machine)
