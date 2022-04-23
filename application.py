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


    
@application.route('/pedal', methods=['GET'])
def report_padelmatch():

    
    result_pedal = []
    result_pedal.append({
            "player": 1,
            "points": 2
        })
    
    return jsonify({
        "pedal": result_pedal
    })

if __name__=="__main__":
    application.run