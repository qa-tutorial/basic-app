'''
Python file that handles hyperlink routing within the site
'''
from application import app
from flask import render_template, redirect, url_for, request
import requests
from os import getenv
import random
from string import ascii_letters

# Route to home page
@app.route('/', methods = ["GET"])
def serial_number():
    serial_number = ''

    for i in range(10):
        if random.randint(0, 1):
            serial_number += random.choice(string.ascii_letters)
        else:
            serial_number += str(random.randint(0, 9))

    return serial_number
