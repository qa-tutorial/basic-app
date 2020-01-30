from application import app
from application.models import Names
from flask import render_template, redirect, url_for, request
import requests
from os import getenv
from sqlalchemy import func

@app.route('/', methods = ["GET"])
def query():
    query_name = Names.query.order_by(func.random()).first())
    return query.name