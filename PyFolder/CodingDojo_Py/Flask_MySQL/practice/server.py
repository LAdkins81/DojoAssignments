from flask import Flask, render_template
from mySQLConnection import MySQLConnector

app = Flask(__name__)
mysql_db = MySQLConnector(app, 'world')

@app.route('/')
def index():
    result = mysql_db.query_db('select * from cities')
    return render_template('index.html', cities=result)

@app.route('/<cc>')
def find_by_country_code(cc):
    criteria = {'code': cc}
    result = mysql_db.query_db('select * from cities where country_code = :code', criteria)
    return render_template('index.html', cities=result)

app.run(debug=True)
