from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

############# users table sql ########################

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Name: ', self.first_name, ' ', self.last_name])

########### tanks table sql #########################

class Tanks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    description = db.Column(db.String(100))

########## tests table sql ############################

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    tank_id = db.Column(db.Integer, db.ForeignKey('tanks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ammonia = db.Column(db.Integer, nullable=False)
    nitrate = db.Column(db.Integer, nullable=False)
    nitrite = db.Column(db.Integer, nullable=False)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
