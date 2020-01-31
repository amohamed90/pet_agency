from models import Pet, db
from app import app

db.drop_all()
db.create_all()

whiskey = Pet(name="Whiskey", species="Mutt", age=6, available=False)
rocky = Pet(name="Rocky", species="Husky", age=6, available=False)

db.session.add(whiskey)
db.session.add(rocky)

db.session.commit()