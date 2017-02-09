from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "anewsession"

@app.route('/')
def index():
    # if 'name' in session:
    #     return redirect('/')
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():

    name = request.form['name']
    location = request.form['location']
    lang = request.form['languages']
    comments = request.form['info']

    if len(request.form['name']) < 1:
        flash("Invalid Login. You must input a name!")
    elif len(request.form['info'])>121:
        flash("Your commments may not exceed 120 characters!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')
    # return render_template("submitted.html", fname=name, place=location, favlang=lang, information=comments)

app.run(debug=True)
