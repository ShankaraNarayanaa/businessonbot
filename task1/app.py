from flask import json, jsonify, request, Flask
import pandas as pd
app = Flask(__name__)
from sqlalchemy import create_engine
engine = create_engine('postgresql://ucjwemyiugimlp:9e712414af84c32436e99f16b18eba7fbd7b040e605830a389452e48faa843a9@ec2-52-212-228-71.eu-west-1.compute.amazonaws.com:5432/dbh3cjjfj4g2jq')

@app.route('/api/branch',methods = ["GET"])
def branch():
    arg = request.args
    offset = int(arg.get('offset') or 0)
    limit = int(arg.get('limit') or 10)
    sql_query = "SELECT * FROM bank_branches where branch like"+ "'%%"+ arg.get('q') +"%%'"+ "ORDER BY branch LIMIT "+ str(limit) + " OFFSET "+ str(offset)
    df = engine.execute(sql_query).fetchall()
    branches = []
    for entity in df:
        data = {'ifsc':entity[0],'bank_id':entity[1],'branch':entity[2],'address':entity[3],'city':entity[4],'district':entity[5],'state':entity[6],'bank_name':entity[7]}
        branches.append(data)
    return jsonify({'branches': branches})

@app.route('/api/search',methods = ["GET"])
def search():
    arg = request.args
    offset = int(arg.get('offset'))
    limit = int(arg.get('limit'))
    if offset == None:
        offset = 0
    if limit == None:
        limit = 10
    sql_query = "SELECT * FROM bank_branches where branch like"+ "'%%"+ arg.get('q') +"%%'"+ "ORDER BY branch LIMIT "+ str(limit) + " OFFSET "+ str(offset)
    df = engine.execute(sql_query).fetchall()
    results = []
    for entity in df:
        data = {
            'ifsc':entity[0],
            'bank_id':entity[1],
            'branch':entity[2],
            'address':entity[3],
            'city':entity[4],
            'district':entity[5],
            'state':entity[6],
            'bank_name':entity[7]
        }
        results.append(data)
    return jsonify({'results': results})