from flask import session
from models.user import Users
from main import db

def create_user(user_lastname, user_firstname, user_gender, user_cpf, user_cep, user_phone, user_cellphone, user_email, user_password):
    # validação dos dados
    #if not _user_firstname or not _user_email or not _user_password:
        #return "Por favor, preencha todos os campos."
    #if User.query.filter_by(email=email).first():
        #return "Email já cadastrado."
    # salvar usuário no banco de dados
    new_user = Users(
                    user_lastname = user_lastname,
                    user_firstname = user_firstname,
                    user_gender = user_gender,
                    user_cpf = user_cpf,
                    user_cep = user_cep,
                    user_phone = user_phone,
                    user_cellphone = user_cellphone,
                    user_email = user_email,
                    user_password = user_password)
    
    db.session.add(new_user)
    db.session.commit()


def authenticte_user(louser_email, louser_password):

    # Cria uma variável local, faz um select no Banco de dados e compara com o input do HTML.
    check = Users.query.filter_by(user_email = louser_email).first()

    print(f'Imprime o varaiável check: => {check}')
    print(louser_email)
    print(louser_password)
    print('Vindo do Banco de Dados')
    print(check.user_email)
    print(check.user_password)

    if check:
        # Origem do HTML for igual a Objeto user .name e .senha
        if (louser_email == check.user_email):
            print('Verificou email')
            if (louser_password == check.user_password):
                print('Verificou a senha')
                # Armazena Usuário
                session['usernamr'] = check.user_firstname

                print(f'Imprime a session do Usuário: {check.user_firstname}')
        else:
            print('Error')
  
