"""
Created on Thu Apr  7 19:03:58 2022

@author: luism
@description: api flask
"""
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

def insert_gym_notes_train():
    return None

def receive_param():
    return None

def get_stasts():
    return None

@app.route("/home", methods=['GET'])
def prueba_api():
    d = {}
    inputchr = str(request.args['query'])
    answer = str(ord(inputchr))
    d['output'] = answer
    return d

if __name__ == "__main__":
    app.run()