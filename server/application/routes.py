from application import app
from flask import render_template, redirect, url_for, request
import requests
from os import getenv

@app.route('/', methods = ["GET"])
def home():
    response = requests.get(getenv("BACKEND_LB")})
    name = response.json()
    machine = getenv("HOSTNAME")
    return render_template('index.html', title = 'Home', name = name, machine = machine)
