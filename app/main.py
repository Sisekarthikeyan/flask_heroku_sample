from flask_cors import CORS
from flask import Flask, render_template, request, Response, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
CORS(app)

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Succesfully deployed on Heroku</h1>"
	
