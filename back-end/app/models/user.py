from main import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    user_lastname= db.Column(db.String(64), nullable = False) 
    user_firstname= db.Column(db.String(64), nullable = False) 
    user_gender = db.Column(db.Boolean, nullable = True)
    user_cpf = db.Column(db.String(11), nullable = False)
    user_cep = db.Column(db.String(8), nullable = False)
    user_phone = db.Column(db.String(10), nullable = True)
    user_cellphone = db.Column(db.String(11), nullable = False)
    user_email = db.Column(db.String(128), nullable = False)
    user_password = db.Column(db.String(64), nullable = False)
    
    
def __repr__(self):
    return '<Name %r>' % self.name