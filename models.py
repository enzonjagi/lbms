from app import db

class User(db.Model):
    """create user table details"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, first_name, username, password):
        """initialise user class"""
        self.first_name = first_name
        self.username = username
        self.password = password
