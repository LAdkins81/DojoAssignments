from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "banana"
mysql = MySQLConnector(app,'mydb')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate')
def authenticate():
    if 'logged_in' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def logged_in():
    query = "SELECT * FROM mydbusers WHERE username = :username and password = :password"
    data = {'username' :request.form['user_name'], 'password' :request.form['password']}
    user = mysql.query_db(query, data)
    if user:
        session['player'] = user[0]['id']
        return redirect('/success')
    if not user:
        flash("You are not a user! Please register!")
        return redirect('/')

@app.route('/success')
def success():
    #yourid = session['player']
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/authenticate')

@app.route('/submit', methods=["POST"])
def submit():
    error_switch = False

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
        error_switch = True

    if len(request.form['first_name']) < 2:
        flash("First name field must be more than 2 characters.")
        error_switch = True
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Invalid first name - name fields may not contain numbers")
        error_switch = True

    if len(request.form['last_name']) < 2:
        flash("Last name field must be more than 2 characters.")
        error_switch = True
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Invalid last name - name fields may not contain numbers")
        error_switch = True

    if request.form['confirmpass'] != request.form['password']:
        flash("Your passwords must match")
        error_switch = True

    if len(request.form['password']) < 8:
        flash("Your password must be greater than 8 characters")
        error_switch = True

    if error_switch == True:
        return redirect('/')
    else:
        query = "INSERT INTO mydbusers (first_name, last_name, created_at, updated_at, email, password, username) VALUES (:first_name, :last_name, NOW(), NOW(), :email, :password, :username)"
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': request.form['password'], 'username': request.form['user_name']}
        mysql.query_db(query, data)

        name = request.form['first_name']

        query2 = "SELECT * FROM mydbusers"
        session_id = mysql.query_db(query2)
        new_id = session_id[0]['id']
        return render_template('success.html', name=name, new_id=new_id)

app.run(debug=True)
