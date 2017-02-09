from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

@app.route('/ninjas')
def ninja_info():
    return render_template('ninja.html')

@app.route('/dojos/new')
def dojos_new():
    return render_template('dojos.html')

app.run(debug=True)
