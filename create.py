## run whilst testing ##
from application import db
from application.models import Users, Tanks

db.drop_all()
db.create_all()
