from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

########### tanks table sql #########################


class Tanks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(25), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ammonia = db.Column(db.Float, nullable=False)
    nitrate = db.Column(db.Float, nullable=False)
    nitrite = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

############# users table sql ########################

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    tanks = db.relationship('Tanks', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'Name: ', self.first_name, ' ', self.last_name])