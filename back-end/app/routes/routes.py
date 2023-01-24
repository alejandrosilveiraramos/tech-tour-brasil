from flask import render_template, request, redirect, url_for, session
from main import app
from controller.user import create_user, authenticte_user 


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/create_user', methods=['GET', 'POST'])
def create_user_route():
    
    if request.method == 'POST':
        louser_lastname = request.form['user_lastName']
        louser_firstname = request.form['user_firstName']
        louser_gender = bool(request.form['user_gender'])
        louser_cpf = request.form['user_cpf']
        louser_cep = request.form['user_cep']
        louser_phone = request.form['user_phone']
        louser_cellphone = request.form['user_cellphone']
        louser_email = request.form['user_email']
        louser_password = request.form['user_password']
        
        create_user(louser_lastname, louser_firstname, louser_gender, louser_cpf, louser_cep, louser_phone, louser_cellphone, louser_email, louser_password)
        
        return redirect(url_for('success'))
    
    return render_template('hotels.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/profile')
def read_user_route():
    return render_template('profile.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Remova o nome de usuário da sessão se estiver lá.
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/authenticte_user', methods=['GET', 'POST'])
def authenticte_user_route():

    if request.method == 'POST':
        louser_email = request.form['user_email']
        louser_password = request.form['user_password']

        authenticte_user(louser_email, louser_password)
        
        return redirect(url_for('success'))

    return render_template('hotels.html')
