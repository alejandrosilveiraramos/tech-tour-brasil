from main import db

class Hotel(db.Model):
    hotel_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    hotel_name = db.Column(db.String(64), nullable = False) 
    hotel_city = db.Column(db.String(64), nullable = False) 
    hotel_coust = db.Column(db.Float, nullable = False)
    
    
    def __init__(self, hotel_id, hotel_name, hotel_city, hotel_coust):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_city = hotel_city
        self.hotel_coust = hotel_coust


def __repr__(self):
    return '<Name %r>' % self.name