from models.user import User
from main import db

def create_user(u_user_lastName, _user_firstName, _user_gender, _user_cpf, _user_cep, _user_phone, _user_cellphone, _user_email, _user_password):
    # validação dos dados
    if not _user_firstName or not _user_email or not _user_password:
        return "Por favor, preencha todos os campos."
    #if User.query.filter_by(email=email).first():
        #return "Email já cadastrado."
    # salvar usuário no banco de dados
    new_user = User(_user_lastName = u_user_lastName, _user_firstName = _user_firstName, _user_gender = _user_gender, _user_cpf = _user_cpf, _user_cep = _user_cep, _user_phone = _user_phone, _user_cellphone = _user_cellphone, _user_email = _user_email, _user_password = _user_password)
    db.session.add(new_user)
    db.session.commit()
