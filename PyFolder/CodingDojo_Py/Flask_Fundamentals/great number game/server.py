from flask import Flask, render_template, session, request, redirect

import random

app = Flask(__name__)
app.secret_key = "cinnamon"

@app.route('/')
def index():
    if 'guess'not in session:
        session['guess'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/authenticate', methods=["POST"])
def guess():

    print session['guess']
    userNum = int(request.form['number'])

    if userNum == session['guess']:
        session['correct'] = True
        # session.clear()
        # print userNum
        return redirect('/')
    elif userNum > session['guess']:
        session['trial'] = "high"
        return redirect('/')
    elif userNum < session['guess']:
        session['trial'] = "low"
        return redirect('/')
    else:
        return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
