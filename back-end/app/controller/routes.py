from flask import render_template
from main import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/hotels')
def hotels():
    return render_template('hotels.html')