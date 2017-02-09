from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "a7656fafe94dae72b1e1487670148412"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    if 'logged_in' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    print "-" * 50, "\nAUTHENTICATING USER"
    password = 'asdf'
    server_username = request.form['html_username']
    server_password = request.form['html_password']

    if server_password == password:
        session['username'] = server_username
        session['logged_in'] = True
        return redirect('/')
    else:
        flash("Invalid Login SUcka!")
        return redirect('/login')

app.run(debug=True)
