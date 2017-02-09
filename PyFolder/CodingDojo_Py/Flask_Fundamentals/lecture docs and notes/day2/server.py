from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    print "\n\nA WEB BROWSER IS REQUESTING A PAGE\n\n"
    return render_template('page1.html')

@app.route('/another')
def logic_for_page_two():
    print "\n\nSECOND PAGE IS BEING REQUESTED AND RETURNED\n\n"
    return render_template('page2.html')

@app.route('/something_else', methods=['POST'])
def logic_for_page_three():
    password = 'this_is_the_password'
    server_username = request.form['html_username']
    server_password = request.form['html_password']

    login_status = False

    if server_password == password:
        login_status = True

    some_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

    return render_template('page3.html', template_username=server_username, success=login_status, numbers=some_list)

app.run(debug=True)
