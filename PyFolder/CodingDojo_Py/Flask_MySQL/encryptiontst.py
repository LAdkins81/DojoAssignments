# md5 encryption

import md5 # imports the md5 module to generate a hash
password = 'password';
# encrypt the password we provided as 32 character string
encrypted_password = md5.new(password).hexdigest();
print encrypted_password; #this will show you the encrypted value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!

#the user being put into database
import md5 # do this at the top of your file where you import modules
@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest();
     insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username,
     :email, :password, NOW(), NOW())"
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)

#the code for when your user is trying to login
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message
<br>

#salt method (salt is the an ingredient and the encryption is the recipe)
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15)) # generates a random string

#storing with salt during the registration process
username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
encrypted_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at)
     VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())"
query_data = { 'username': username, 'email': email, 'encrypted_pw': encrypted_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)

#example of using salt during the registration process
username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
encrypted_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at)
     VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())"
query_data = { 'username': username, 'email': email, 'encrypted_pw': encrypted_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)

#and nifty stuff needed to store with salt
email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
query_data = {'email': email}
user = mysql.query_db(user_query, query_data)
if user[0]:
 encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
 if user[0]['password'] == encrypted_password:
  # this means we have a successful login!
 else:
     # invalid password!
else:
  # invalid email!

#using bcrypt in flask
from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'my_database_here')
# this will load a page that has 2 forms one for registration and login
@app.route('/', methods=['GET'])
def index():
 return render_template('index.html')
# we are going to add functions to create new users and login users

#generating new passwords hash using bcrypt
@app.route('/create_user', methods=['POST'])
def create_user():
 email = request.form['email']
 username = request.form['username']
 password = request.form['password']
 # run validations and if they are successful we can create the password hash with bcrypt
 pw_hash = bcrypt.generate_password_hash(password)
 # now we insert the new user into the database
 insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
 query_data = { 'email': email, 'username': username, 'pw_hash': pw_hash }
 mysql.query_db(insert_query, query_data)
 # redirect to success page

#check the password hash
password = 'password'
pw_hash = bcrypt.generate_password_hash(password)
test_password_1 = 'thisiswrong'
bcrypt.check_password_hash(pw_hash, test_password_1) # this will return false
test_password_2 = 'password'
bcrypt.check_password_hash(pw_hash, test_password_2) # this will return true

#this is what bcrypt will need for login
@app.route('/login', methods=['POST'])
def login():
 email = request.form['email']
 password = request.form['password']
 user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
 query_data = { 'email': email }
 user = mysql.query_db(user_query, query_data) # user will be returned in a list
 if bcrypt.check_password_hash(user[0]['pw_hash'], password):
  # login user
 else:
  # set flash error message and redirect to login page
