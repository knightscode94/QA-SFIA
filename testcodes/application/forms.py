from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Places, Rounding
from wtforms_sqlalchemy.fields import QuerySelectField
from application.models import Users, Tanks, Tests
from flask_login import current_user

##### register form #################

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)])

    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)])

    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()])

    submit = SubmitField('Create Account')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

############ register tanks ##############

class RegistrationTankForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)])

    description = StringField('Decription',
        validators = [
            DataRequired(),
            Length(min=0, max=100)])

    submit = SubmitField('Create Tank')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')
    tank_select_field = SelectField(label="Tanks", coerce=int)

############### submit tests ########################
def tank_query():
    return Tanks.query
class TestsForm(FlaskForm):
    tank_name = QuerySelectField(query_factory=tank_query, allow_blank=False)

    ammonia = DecimalField('Ammonia',
        Places=2, Rounding=None,
        validators = DataRequired())

    nitrate = DecimalField('Nitrate',
        Places=2, Rounding=None,
        validators = DataRequired())

    nitrite = DecimalField('Nitrite',
        Places=2, Rounding=None,
        validators = DataRequired())

    submit = SubmitField('Create Tank')

################ login form ##################

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()])

    remember = BooleanField('Remember Me')
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

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')