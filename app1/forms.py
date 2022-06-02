from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, ValidationError
from wtforms.validators import Email, EqualTo, DataRequired

# https://wtforms.readthedocs.io/en/3.0.x/crash_course/


class CustomUsernameForm(FlaskForm):
    email = EmailField("Input your email address", validators=[DataRequired(), Email()])