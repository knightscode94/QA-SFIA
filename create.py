## run whilst testing ##
from application import db
from application.models import Users, Tanks

db.drop_table('tanks')
db.drop_table('users')
db.create_all()
