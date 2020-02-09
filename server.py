from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL

app = Flask(__name__)

app.secret_key = 'password'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return(render_template('index.html'))

@app.route('/add', methods=['POST'])
def add():

    if len(request.form['FN']) < 2:
    	flash("Please enter a first name")
    if len(request.form['LN']) < 2:
    	flash("Please enter a last name")
    if len(request.form['EM']) < 2:
    	flash("Occupation should be at least 2 characters")    
    if len(request.form['PW']) < 2:
    	flash("Occupation should be at least 2 characters")     
    if not '_flashes' in session.keys():
        flash("Friend successfully added!") 

    query = 'INSERT INTO registrations (first_name, last_name, email, password, updated_at, created_at) VALUES (%(FN)s, %(LN)s, %(EM)s, %(PW)s, NOW(), NOW())'
    data = {
        'FN' : request.form['FN'], 
        'LN' : request.form['LN'],
        'EM' : request.form['EM'],
        'PW' : request.form['PW'],
    }
    print(data)
    test = connectToMySQL('registration_with_email')
    test.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)