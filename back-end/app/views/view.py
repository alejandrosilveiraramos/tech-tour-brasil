from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.user import Users
from models.hotel import Hotel
from models.history import History

@app.route('/')
def home():
    if 'username' not in session or session['username'] is None:

        return render_template('home.html', reg_pro = 'register')
    else:
        return render_template('home.html', reg_pro = 'profile')


@app.route('/register')
def register():
    if 'username' not in session or session['username'] is None:

        return render_template('register.html', reg_pro = 'register')
    else:
        return redirect(url_for('home', reg_pro = 'profile'))


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():

    if 'username' not in session or session['username'] is None:

        lo_user_lastname = request.form['user_lastName']
        lo_user_firstname = request.form['user_firstName']
        lo_user_gender = bool(request.form['user_gender'])
        lo_user_cpf = request.form['user_cpf']
        lo_user_cep = request.form['user_cep']
        lo_user_phone = request.form['user_phone']
        lo_user_cellphone = request.form['user_cellphone']
        lo_user_email = request.form['user_email']
        lo_user_password = request.form['user_password']

        # Faz um select no banco para ver se o usuário já está cadastrado.    
        lo_novo_usuario = Users.query.filter_by(user_cpf = lo_user_cpf).first()

        if lo_novo_usuario:
            # Usuário já cadastrado, apresentr uma tela de mensagem
            return redirect(url_for('register', reg_pro = 'register'))
        else:

            lo_novo_usuario = Users(
                                    user_lastname = lo_user_lastname,
                                    user_firstname = lo_user_firstname,
                                    user_gender = lo_user_gender,
                                    user_cpf = lo_user_cpf,
                                    user_cep = lo_user_cep,
                                    user_phone = lo_user_phone,
                                    user_cellphone = lo_user_cellphone,
                                    user_email = lo_user_email,
                                    user_password = lo_user_password)
        
            db.session.add(lo_novo_usuario)
            db.session.commit()

            # Armazena Usuário
            session['username'] = lo_novo_usuario.user_firstname

            # Ou fazer uma tela de Registo com sucesso.            
            return redirect(url_for('success', reg_pro = 'register'))
        
    else:
    
        return redirect(url_for('home', reg_pro = 'profile'))


@app.route('/success')
def success():

    if 'username' not in session or session['username'] is None:

        return redirect(url_for('home', reg_pro = 'register'))
    else:
        return render_template('success.html', reg_pro = 'profile')


@app.route('/login')
def login():
    if 'username' not in session or session['username'] is None:

        lo_proximo = request.args.get('proximo')

        return render_template('login.html', reg_pro = 'register', proximo = lo_proximo)
    else:
        return redirect(url_for('home', reg_pro = 'profile'))


@app.route('/authenticte_user', methods=['GET', 'POST'])
def authenticte_user():

    if 'username' not in session or session['username'] is None:
        # Cria uma variável local, faz um select no Banco de dados e compara com o input do HTML.
        lo_check = Users.query.filter_by(user_email = request.form['user_email']).first()

        if lo_check:
            # Origem do HTML for igual a Objeto user .email e .senha
            if (request.form['user_email'] == lo_check.user_email) and (request.form['user_password'] == lo_check.user_password):
                # Armazena Usuário
                session['username'] = lo_check.user_firstname

                return render_template('login_success.html', reg_pro = 'profile')
            else:

                return redirect(url_for('login', reg_pro = 'register'))

    else:

        return redirect(url_for('home', reg_pro = 'profile'))


@app.route('/logout')
def logout():
    # Remova o nome de usuário da sessão se estiver lá.
    session['username'] = None

    return redirect(url_for('home'))


@app.route('/profile')
def read_user():

    if 'username' not in session or session['username'] is None:

        return render_template('home.html', reg_pro = 'register')
    else:
        # Cria um Objeto com o select do banco de dados onde 'user_firstname' é igual a usuário logado.
        lo_usuario = Users.query.filter_by(user_firstname = session["username"]).first()

        # Somente remover, Só imprime no terminal objeto.nome do usuario.
        print(lo_usuario.user_firstname)

        # Renderiza a página HTML pasando como parametros: a página html, link e o objeto usuario. 
        return render_template('profile.html', reg_pro = 'profile', usuario = lo_usuario)


@app.route('/update', methods = ['POST'])
def update_user():
    
    if 'username' not in session or session['username'] is None:

        return render_template('home.html', reg_pro = 'register')
    else:

        lo_update_user = Users.query.filter_by(user_id = request.form['id_user']).first()

        lo_update_user.user_lastname = request.form['user_lastName']
        lo_update_user.user_firstname = request.form['user_firstName']
        lo_update_user.user_gender = bool(request.form['user_gender'])
        lo_update_user.user_cpf = request.form['user_cpf']
        lo_update_user.user_cep = request.form['user_cep']
        lo_update_user.user_phone = request.form['user_phone']
        lo_update_user.user_cellphone = request.form['user_cellphone']
        lo_update_user.user_email = request.form['user_email']
        lo_update_user.user_password = request.form['user_password']
    
        db.session.add(lo_update_user)
        db.session.commit()

        # Ou fazer uma tela de Registo com sucesso.            
        return render_template('update_success.html', reg_pro = 'profile')


@app.route("/delete/<int:id>")
def delete_user(id):
    
    if 'username' not in session or session['username'] is None:

        return render_template('home.html', reg_pro = 'register')
    else:
        lo_delete_user = Users.query.filter_by(user_id = id).delete()
        db.session.commit()

        session['username'] = None

        return redirect(url_for("home"))


@app.route('/hotel', methods = ['POST'])
def read_hotel():

    if 'username' not in session or session['username'] is None:
        return render_template('home.html', reg_pro = 'register')
    else:

        lo_modify = request.form['hotel_city'].title()

        # Cria um Objeto com o select do banco de dados onde 'hotel_name' é igual a hotel_name vindo do HTML.
        lo_hotel = Hotel.query.filter_by(hotel_city = lo_modify).order_by(Hotel.hotel_coust)

        # Interação para imprimir os hoteis.
        for hoteis in lo_hotel:
            print(f'Id do Hotel => {hoteis.hotel_id}')
            print(f'Name do Hotel => {hoteis.hotel_name}')
            print(f'Cidade do Hotel => {hoteis.hotel_city}')
            print(f'Diária do Hotel => {hoteis.hotel_coust}')

        # Renderiza a página HTML pasando como parametros: a página html, link e o objeto usuario. 
        return render_template('hotels.html', reg_pro = 'profile', obj_hotel = lo_hotel)


@app.route('/hotel_link')
def hotel_link():

    if 'username' not in session or session['username'] is None:

        return render_template('home.html', reg_pro = 'register')
    else:

        #lo_modify = request.form['hotel_city'].title()

        # Cria um Objeto com o select do banco de dados onde 'hotel_name' é igual a hotel_name vindo do HTML.
        lo_hotel = Hotel.query.filter_by().order_by(Hotel.hotel_coust)

        # Interação para imprimir os hoteis.
        #for hoteis in lo_hotel:
        #    print(f'Id do Hotel => {hoteis.hotel_id}')
        #    print(f'Name do Hotel => {hoteis.hotel_name}')
        #    print(f'Cidade do Hotel => {hoteis.hotel_city}')
        #    print(f'Diária do Hotel => {hoteis.hotel_coust}')

        # Renderiza a página HTML pasando como parametros: a página html, link e o objeto usuario. 
        return render_template('hotels.html', reg_pro = 'profile', obj_hotel = lo_hotel)
