from app import app
from app import db
from app import User
db.create_all()
neto = User(username='neto', email='neto@example.com')
db.session.add(neto)
db.session.commit()
print(User.query.all())