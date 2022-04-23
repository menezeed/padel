#import mysql.connector
import os
from flask import jsonify
from flask import redirect
from flask import Flask
application = Flask(__name__)

base_path = os.environ.get('STATIC_URL', application.static_url_path)

@application.route('/')
def root():
    return redirect(base_path + '/Index.html')


    
@application.route('/pedal', methods=['GET'])
def report_padelmatch():

    
    result_pedal = []
    result_pedal.append({
            "player": "player 1",
            "points": "3"
        })
    result_pedal.append({
            "player": "player 2",
            "points": "7"
        })
    return jsonify({
        "pedal": result_pedal
    })

if __name__=="__main__":
    application.run(debug=True)