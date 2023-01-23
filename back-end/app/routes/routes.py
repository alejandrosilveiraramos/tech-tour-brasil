from flask import render_template, request, redirect, url_for
from main import app
from controller.user import create_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/create_user", methods=["GET", "POST"])
def create_user_route():
    
    if request.method == "POST":
        _user_lastName = request.form["user_lastName"]
        _user_firstName = request.form["user_firstName"]
        _user_gender = request.form["user_gender"]
        _user_cpf = request.form["user_cpf"]
        _user_cep = request.form["user_cep"]
        _user_phone = request.form["user_phone"]
        _user_cellphone = request.form["user_cellphone"]
        _user_email = request.form["user_email"]
        _user_password = request.form["user_password"]
        
        create_user(_user_lastName, _user_firstName, _user_gender, _user_cpf, _user_cep, _user_phone, _user_cellphone, _user_email, _user_password)
        
        return redirect(url_for("success"))
    
    return render_template("hotels.html")

@app.route("/success")
def success():
    return "Usuário criado com sucesso!"

@app.route('/user')
def user():
    return render_template('user.html')
