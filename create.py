## run whilst testing ##
from application import db
from application.models import Users, Tanks

db.table.drop('tanks')
db.table.drop('users')
db.create_all()
