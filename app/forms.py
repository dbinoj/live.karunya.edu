from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from app import models, utils
from sqlalchemy import func


### VALIDATORS ###

class LoginValidator(object):
    def __init__(self, pw_field, message_username = "The username or password is incorrect.", message_password = "The username or password is incorrect."):
        self.pw_field = pw_field
        self.message_username = message_username
        self.message_password = message_password

    def __call__(self, form, field):
        u = models.User.query.filter(func.lower(models.User.username) == func.lower(field.data)).first()
        if not u:
            raise ValidationError(self.message_username)
        elif not utils.verify_password(u.password, form[self.pw_field].data):
            raise ValidationError(self.message_password)

class LoginForm(Form):
    username = StringField('username', validators=[LoginValidator("password")])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
