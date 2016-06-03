import getpass

from app import db
from app.models import User

username = raw_input("Please enter username: ")
password = getpass.getpass("Please enter password: ")
realname = raw_input("Please enter full name: ")
email = raw_input("Please enter email: ")

user = User(username, password, realname, email)
db.session.add(user)
db.session.commit()
print ("User %s added. User ID: %s" % (user.username, str(user.id)))
