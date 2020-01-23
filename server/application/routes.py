'''
Python file that handles hyperlink routing within the site
'''
from application import app
from flask import render_template, redirect, url_for, request

# Route to home page
@app.route('/', methods = ["GET"])
def home():
    return render_template('index.html', title = 'Home')
