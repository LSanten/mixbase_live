from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User

class RegistrationForm(FlaskForm):
    #First string is name of input field in browser
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username): #catches if username is already in database

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('The username you chose is taken.')

    def validate_email(self, email): #catches if email is already in database

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('The email you chose is taken.')

class LoginForm(FlaskForm):
    #First string is name of input field in browser
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign Up')

class PairForm(FlaskForm): #Form for saving transition in database
    firstname = StringField('Name A', validators=[DataRequired()])

    firstartist = StringField('Artist A', validators=[DataRequired()])

    #secondname = StringField('Name B', validators=[DataRequired()])
    secondname = StringField('Name B') #this is changed to allow single song inputs

    #secondartist = StringField('Artist B', validators=[DataRequired()])
    secondartist = StringField('Artist B')

    comment = TextAreaField('Any comments?')

    submit = SubmitField('Enter Transition')
