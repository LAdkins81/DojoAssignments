from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "banana"

@app.route('/')
def counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    return render_template('index.html')

@app.route('/plustwo')
def plustwo():
    session['visits'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
