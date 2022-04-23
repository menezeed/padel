#import mysql.connector
from flask import jsonify
from flask import redirect
from flask import Flask
application = Flask(__name__)

database = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=srv_padel_uat;UID=root;PWD=London@990'
base_path = 'http://127.0.0.1:5000'


@application.route('/')
def root():
    return 'test'