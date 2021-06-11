from flask import Flask, jsonify, request, render_template, session, redirect, url_for, send_from_directory,json
from functools import wraps
import uuid
import os
import bcrypt
from pymongo import MongoClient
import requests

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

GLOBAL_SERVER_LINK = 'http://portfolio-manager-backend-server:3000/'
@app.route('/')
def home():
    r = requests.get(url = GLOBAL_SERVER_LINK)
    data = r.json()
    # data = {'name': 'Hello World! Boiii'}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response

# @app.route("/create_link_token", methods=['POST'])
# def create_link_token():
#     # Get the client_user_id by searching for the current user
#     user = User.find(...)
#     client_user_id = user.id
#     # Create a link_token for the given user
#     response = client.LinkToken.create({
#       'user': {
#         'client_user_id': client_user_id,
#       },
#       'products': ["auth"],
#       'client_name': 'Plaid Test App',
#       'country_codes': ['US'],
#       'language': 'en',
#       'webhook': 'https://webhook.sample.com',
#     })
#     # Send the data to the client
#     return jsonify(response)