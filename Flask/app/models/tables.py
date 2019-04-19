from app import db
from datetime import date

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))
    admin = db.Column(db.Boolean)

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def get_name(self):
        return str(self.username)

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin

    def __repr__(self):
        return "<User %r>" % self.username
