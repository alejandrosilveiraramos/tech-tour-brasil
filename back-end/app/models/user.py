from main import db

class User(db.Model):
    _user_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    _user_lastName= db.Column(db.String(64), nullable = False) 
    _user_firstName= db.Column(db.String(64), nullable = False) 
    _user_gender = db.Column(db.Boolean, nullable = True)
    _user_cpf = db.Column(db.String(11), nullable = False)
    _user_cep = db.Column(db.String(8), nullable = False)
    _user_phone = db.Column(db.String(10), nullable = True)
    _user_cellphone = db.Column(db.String(11), nullable = False)
    _user_email = db.Column(db.String(128), nullable = False)
    _user_password = db.Column(db.String(64), nullable = False)
    
    
    def __init__(self, user_id, user_lastName, user_firstName, user_gender, user_cpf, user_cep, user_phone, user_cellphone, user_email, user_password):
        self.user_id = user_id
        self.user_lastName = user_lastName
        self.user_firstName = user_firstName
        self.user_gender = user_gender
        self.user_cpf = user_cpf
        self.user_cep = user_cep
        self.user_phone = user_phone
        self.user_cellphone = user_cellphone
        self.user_email = user_email
        self.user_password = user_password


    def __repr__(self):
        return '<Name %r>' % self.name