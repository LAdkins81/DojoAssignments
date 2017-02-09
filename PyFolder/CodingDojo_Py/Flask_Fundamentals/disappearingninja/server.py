from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secretkey = "banana"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas/')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninjas_color(color):
    valid = False
    if color != "red" or color != "blue" or color != "orange" or color != "purple":
        valid = True
    return render_template('ninjas.html', color=color, valid=valid)

app.run(debug=True)
