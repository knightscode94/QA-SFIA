from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import Users, Tanks
from flask_login import current_user

##### register form #################


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=2, max=30)])

    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=2, max=30)])

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()])

    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

############ register tanks tests ##############


class TanksForm(FlaskForm):
    name = StringField('Name',
                       validators=[
                           DataRequired(),
                           Length(min=2, max=30)])

    description = StringField('Description',
                              validators=[
                                  Length(max=100)])
    ammonia = DecimalField('Ammonia',
                           places=2, rounding=None)

    nitrate = DecimalField('Nitrate',
                           places=2, rounding=None)

    nitrite = DecimalField('Nitrite',
                           places=2, rounding=None)

    submit = SubmitField('Create Tank Test')

################ login form ##################


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()])

    submit = SubmitField('Login')

################# update account #########################


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=4, max=20)
                             ])
    last_name = StringField('Last Name',
                            validators=[
                                DataRequired(),
                                Length(min=4, max=25)
                            ])
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
