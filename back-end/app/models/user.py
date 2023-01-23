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
    
    
    def __init__(self, _user_lastName, _user_firstName, _user_gender, _user_cpf, _user_cep, _user_phone, _user_cellphone, _user_email, _user_password):
        self._user_lastName = _user_lastName
        self._user_firstName = _user_firstName
        self._user_gender = _user_gender
        self._user_cpf = _user_cpf
        self._user_cep = _user_cep
        self._user_phone = _user_phone
        self._user_cellphone = _user_cellphone
        self._user_email = _user_email
        self._user_password = _user_password


    def __repr__(self):
        return '<Name %r>' % self.name