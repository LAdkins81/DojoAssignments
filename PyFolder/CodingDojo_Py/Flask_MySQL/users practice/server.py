from flask import Flask, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
@app.route('/')
def users():
    result = mysql.query_db("SELECT first_name, last_name FROM mydbusers")
    return render_template('index.html', users=result)

# @app.route('/names/<users>')
# def find_by_name(users):
#     criteria = {'user_name': first_name}
#     result = mysql.query_db("SELECT * FROM mydbusers where user_name = :user_name", criteria)
#     return render_template('index.html', users=result)

app.run(debug=True)
