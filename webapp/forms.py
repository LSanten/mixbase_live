from flask_wtf import FlaskForm, RecaptchaField
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
    guestname = StringField('Your name')

    firstname = StringField('Title A <b>*</b>', validators=[DataRequired()])

    firstartist = StringField('Artist A <b>*</b>', validators=[DataRequired()])

    #secondname = StringField('Name B', validators=[DataRequired()])
    secondname = StringField('Title B <b>*</b>', validators=[DataRequired()]) #this is changed to allow single song inputs

    #secondartist = StringField('Artist B', validators=[DataRequired()])
    secondartist = StringField('Artist B <b>*</b>', validators=[DataRequired()])

    comment = TextAreaField('Any notes?')

    submit = SubmitField('Save Transition')

    firstgenre = StringField('Genre of Song A')

    secondgenre = StringField('Genre of Song B')

    recaptcha = RecaptchaField()

class SingleForm(FlaskForm): #Form for saving single song (NOT transition) in database
    guestname = StringField('Your name')

    firstname = StringField('Title A <b>*</b>', validators=[DataRequired()])

    firstartist = StringField('Artist A <b>*</b>', validators=[DataRequired()])

    comment = TextAreaField('Any notes?')

    submit = SubmitField('Save Song')

    firstgenre = StringField('Genre')

    recaptcha = RecaptchaField()
