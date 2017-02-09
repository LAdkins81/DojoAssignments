
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/success')
def success():
    return render_template('index.html', name="Laura")
@app.route('/stars')
def print_stars():
    return "****************"

def hello_world():
    return render_template('index.html')
app.run(debug=True)
