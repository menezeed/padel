import os
from flask import jsonify
from flask import redirect
from flask import Flask

import random

application = Flask(__name__)

base_path = os.environ.get('STATIC_URL', application.static_url_path)

@application.route('/')
def root():
    return "Oi!!"
    return redirect(base_path + '/Index.html')

@application.route('/pedal', methods=['GET'])
def report_padelmatch():

    
    result_pedal = []

    dateTimeObj = random.randrange(1, 9)
    result_pedal.append({
            "player": "player 1",
            "points": dateTimeObj
        })

    dateTimeObj = random.randrange(10, 90)
    result_pedal.append({
            "player": "player 2",
            "points": dateTimeObj
        })
    return jsonify({
        "pedal": result_pedal
    })

if __name__=="__main__":
    application.run



#def hello_world():
#    conn = pyodbc.connect(database)
#    return 'Sup. Subscribe'