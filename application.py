#import os
#import pyodbc
#import mysql.connector
from flask import jsonify
from flask import redirect
from flask import Flask
application = Flask(__name__)

@application.route('/')
def root():
    return 'Oi Tu Again'