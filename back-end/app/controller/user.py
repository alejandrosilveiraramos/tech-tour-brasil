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
