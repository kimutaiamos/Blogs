from wtforms.validators import required,Email,EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError,BooleanField
from flask_wtf import FlaskForm
from ..models import User
