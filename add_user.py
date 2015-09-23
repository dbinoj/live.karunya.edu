from app import db
from app.utils import hash_password, verify_password
from app.models import User

new_user = User("admin","admin","admin@karunya.edu")

db.session.add(new_user)
