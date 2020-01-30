from application import app
from application.models import Names
from flask import jsonify
from sqlalchemy import func

@app.route('/', methods = ["GET"])
def query():
    query_name = Names.query.order_by(func.random()).first())
    return jsonify(query.name)
