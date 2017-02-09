from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "banana"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]+$')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    if len(request.form['email']) == 0:
        flash("Email field cannot be empty.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")

    if len(request.form['fname']) == 0:
        flash("First name field cannot be empty.")
    elif not NAME_REGEX.match(request.form['fname']):
        flash("Invalid first name")

    if len(request.form['lname']) == 0:
        flash("Last name field cannot be empty.")
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Invalid last name")

    if len(request.form['birthday']) == 0:
        flash("Brithday field cannot be empty")
    # elif not DATE_REGEX.match(reqeust.form['birthday']):
    #     flash("Please submit a valid date")

    if len(request.form['confirmpass']) == 0:
        flash("Confirmation field cannot be empty.")
    elif request.form['confirmpass'] != request.form['password']:
        flash("Your passwords must match")

    if len(request.form['password']) == 0:
        flash("Password field cannot be empty.")
    elif len(request.form['password']) < 8:
        flash("Your password must be greater than 8 characters")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Your password must have at least one number and one letter")

    else:
        flash("Thank you for submitting your form!")
        return redirect('/')

    return redirect('/')

app.run(debug=True)
