## run whilst testing ##
from application import db
from application.models import Users, Tanks

db.drop_table(Tanks)
db.drop_table(Users)
db.create_all()
