from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "73ec77d9dd1479cb7616a2f93652af66"
mysql = MySQLConnector(app,'the_wall_db')

import md5

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('log_reg.html')

@app.route('/login')
def logged_in():
    if 'logged_in' in session:
        return redirect('/thewall')
    if 'logged_in' not in session:
        return redirect('/')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    password = md5.new(request.form['password']).hexdigest();
    query = "SELECT * FROM users WHERE email = :email and password = :password"
    data = {'email' : request.form['email'], 'password' : password}
    user = mysql.query_db(query, data)
    if user:
        session['name'] = user[0]['first_name']
        session['userid'] = user[0]['id']
        return redirect('/thewall')
    if not user:
        flash('OOPS! Login failed!')
        return redirect('/')

@app.route('/thewall')
def thewall():
    name = session['name']
    query = "SELECT * FROM users JOIN messages WHERE messages.user_id = users.id"
    result = mysql.query_db(query)
    query2 = "SELECT * FROM users JOIN comments WHERE comments.user_id = users.id"
    commresult = mysql.query_db(query2)
    return render_template('index.html', name=name, selectors=result, commresult=commresult)

@app.route('/postroute', methods=['POST'])
def message():
    query = "INSERT INTO messages(messages, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
    data = {'message' : request.form['message'],
            'user_id' : session['userid']}
    mysql.query_db(query,data)
    return redirect('/thewall')

@app.route('/commentroute/<mesid>', methods=['POST'])
def comment(mesid):
    query = "INSERT INTO comments(message_id, comment, created_at, updated_at, user_id) VALUES (:message_id, :comment, NOW(), NOW(), :user_id)"
    data1 = {
        'comment' : request.form['comment'],
        'message_id' : mesid,
        'user_id' : session['userid']
        }
    mysql.query_db(query, data1)
    return redirect('/thewall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/submit', methods=['POST', 'GET'])
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
        password = md5.new(request.form['password']).hexdigest();
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at, email, password) VALUES (:first_name, :last_name, NOW(), NOW(), :email, :password)"
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': password}
        newuser = mysql.query_db(query, data)
        flash("You've successfully registered! Please log-in!")
        return redirect('/')


app.run(debug=True)
