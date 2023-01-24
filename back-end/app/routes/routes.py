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
        user_lastname = request.form["user_lastName"]
        user_firstname = request.form["user_firstName"]
        user_gender = bool(request.form["user_gender"])
        user_cpf = request.form["user_cpf"]
        user_cep = request.form["user_cep"]
        user_phone = request.form["user_phone"]
        user_cellphone = request.form["user_cellphone"]
        user_email = request.form["user_email"]
        user_password = request.form["user_password"]
        
        create_user(user_lastname, user_firstname, user_gender, user_cpf, user_cep, user_phone, user_cellphone, user_email, user_password)
        
        return redirect(url_for("success"))
    
    return render_template("hotels.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/profile")
def read_user_route():
    return render_template("profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/user')
def user():
    return render_template('user.html')
