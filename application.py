import os
from email.mime import application
import pyodbc
import mysql.connector
from flask import jsonify
from flask import redirect
from flask import Flask
application = Flask(__name__)

database = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=srv_padel_uat;UID=root;PWD=London@990'

base_path = 'http://127.0.0.1:5000'



@application.route('/')
def root():
    return redirect(base_path + '/static/Index.html')

@application.route('/pedal', methods=['GET'])
def report_padelmatch():

    conn = mysql.connector.connect(user='root', password='London@990',
                              host='127.0.0.1', database='srv_padel_uat',
                              auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    strSQL = 'select * from match_data;'
    cursor.execute(strSQL)
    row = cursor.fetchone()
    result_pedal = []
    while row:
        result_pedal.append({
            "player": row[0],
            "points": row[1]
        })
        row = cursor.fetchone()
    conn.close

    return jsonify({
        "pedal": result_pedal
    })

if __name__=="__main__":
    application.run



#def hello_world():
#    conn = pyodbc.connect(database)
#    return 'Sup. Subscribe'