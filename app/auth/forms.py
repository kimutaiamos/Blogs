from wtforms import validators
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError,BooleanField
from flask_wtf import FlaskForm
from ..models import User


class RegistrationForm(FlaskForm):
    """
    registration form class thats pass in the details for validation
    """
    email = StringField('your email address', validators=[DataRequired(), Email()])
    username = StringField('your username', validators=[DataRequired()])
    Password = PasswordField('password', validators=[DataRequired(), EqualTo('password', message='password must match')])
    Password_confirm = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('sign up')



    def validate_email(self,data_field):
        """
        functions that takes in the data field and checks the database to confirm user validation
        """
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')


    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('that username is already taken or incorrect spellings')
    

class loginForm(FlaskForm):
    email = StringField('your email address', validators=[DataRequired(),Email()])
    password = StringField('password', validators=[DataRequired()])
    remember = BooleanField('remeber me')
    submit = SubmitField('Sign In')




