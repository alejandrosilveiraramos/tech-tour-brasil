from main import db
from models.user import User
from models.hotels import Hotel

class History(db.Model):
    _history_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    _history_fk_id_user = db.Column(db.Integer, db.ForeignKey(User._user_id), nullable = False)
    _history_fk_id_hotel = db.Column(db.Integer, db.ForeignKey(Hotel._hotel_id), nullable = False)
    _history_check_in = db.Column(db.Date, nullable = False)
    _history_check_out = db.Column(db.Date, nullable = False)


    def __init__(self, history_id, history_fk_id_user, history_fk_id_hotel, history_check_in, history_check_out):
        self.hohistory_id = history_id
        self.history_fk_id_user = history_fk_id_user
        self.history_fk_id_hotel = history_fk_id_hotel
        self.history_check_in = history_check_in
        self.history_check_out = history_check_out


    def __repr__(self):
        return '<Name %r>' % self.name
