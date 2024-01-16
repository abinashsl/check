from flask import Flask, render_template, request, redirect, url_for, make_response
from db import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    username = request.form['username']
    password = request.form['password']

    out = search(username, password)

    if out == 'Logged IN':
        # Redirect to another webpage
        return redirect(url_for('success'))
    elif out == 'Check Password':
        return redirect(url_for('pwderror'))
    else:
        # Values are incorrect, you can handle it as needed
        return render_template('error.html')

@app.route('/success')
def success():
    return render_template('questions.html')
    

@app.route('/pwderror')
def pwderror():
    return render_template('pwderror.html')

@app.route('/submit', methods=['POST'])
def submit():
    return 'Thanks! for Submission. Check Your mail for Results.'

if __name__ == '__main__':
    app.run(debug=True)