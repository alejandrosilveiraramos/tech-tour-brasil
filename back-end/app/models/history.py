from main import db
from models.user import Users
from models.hotel import Hotel

class History(db.Model):
    history_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    history_fk_id_user = db.Column(db.Integer, db.ForeignKey(Users.user_id), nullable = False)
    history_fk_id_hotel = db.Column(db.Integer, db.ForeignKey(Hotel.hotel_id), nullable = False)
    history_check_in = db.Column(db.Date, nullable = False)
    history_check_out = db.Column(db.Date, nullable = False)


def __repr__(self):
    return '<Name %r>' % self.name
