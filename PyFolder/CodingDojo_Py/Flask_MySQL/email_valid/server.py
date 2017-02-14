from flask import Flask, render_template, redirect, flash, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "banana"
mysql = MySQLConnector(app, 'email_valid')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'activities' not in session:
        session["activities"] = []
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def submit():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email not valid!")
        return redirect('/')
    else:
        email = request.form['email']
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        result = mysql.query_db("SELECT email, created_at FROM emails")

        return render_template('success.html', email = email, selectors=result)

# @app.route('/delete/<id>', methods=['POST'])
# def delete(id):
#     criteria = {code: id}
#     query1=mysql.query_db("DELETE from emails WHERE id = :id", criteria)
#
#     return redirect('/success', criteria)

app.run(debug="True")
