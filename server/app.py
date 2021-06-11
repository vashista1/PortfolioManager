from flask import Flask, jsonify, request, render_template, session, redirect, url_for, send_from_directory, json
from functools import wraps
from flask_restful import Resource, Api
import uuid
import os
import bcrypt
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
# api = Api(app)

# client = MongoClient("mongodb://db:27017")
# employee_data = client.employee_data
# employees = employee_data.employees

@app.route('/')
def home():
    data = {'name': 'Hello World! this is diff son'}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response


# class Employees(Resource):
#     def get(self):
#         conn = db_connect.connect()  # connect to database
#         # This line performs query and returns json result
#         query = conn.execute("select * from employees")
#         # Fetches first column that is Employee ID
#         return {'employees': [i[0] for i in query.cursor.fetchall()]}


# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute(
#             "select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple(query.keys()), i))
#                            for i in query.cursor]}
#         return jsonify(result)


# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute(
#             "select * from employees where EmployeeId =%d " % int(employee_id))
#         result = {'data': [dict(zip(tuple(query.keys()), i))
#                            for i in query.cursor]}
#         return jsonify(result)


# api.add_resource(Employees, '/employees')  # Route_1
# api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3


# def load_data():
#     employee_list = ({
#         "id": uuid.uuid4().hex,
#         "name": "Watch",
#         "quantity": 10,
#         "price": 200,
#         "discontinued": False,
#         "tags": ["Fashion", "Utility", "Official"]
#     }, {
#         "id": uuid.uuid4().hex,
#         "name": "Cup",
#         "quantity": 15,
#         "price": 20,
#         "discontinued": False,
#         "tags": ["Home", "Decor"]
#     }, {
#         "id": uuid.uuid4().hex,
#         "name": "Camera Roll",
#         "quantity": 25,
#         "price": 18,
#         "discontinued": False,
#         "tags": ["Home", "Decor"]
#     }, {
#         "id": uuid.uuid4().hex,
#         "name": "Office Desk",
#         "quantity": 3,
#         "price": 20,
#         "discontinued": False,
#         "tags": ["Home", "Decor", "Work"]
#     }, {
#         "id": uuid.uuid4().hex,
#         "name": "Telephone",
#         "quantity": 9,
#         "price": 30,
#         "discontinued": False,
#         "tags": ["Home", "Office"]
#     }, {
#         "id": uuid.uuid4().hex,
#         "name": "Analog",
#         "quantity": 3,
#         "price": 250,
#         "discontinued": True,
#         "tags": ["Fashion", "Utility", "Official"]
#     }
#     )
#     employees.insert_many(employee_list)
