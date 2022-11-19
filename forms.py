from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DecimalRangeField, FloatField
from wtforms.validators import DataRequired, URL, NumberRange
from flask_ckeditor import CKEditorField


# #WTForm

class Cafe(FlaskForm):
    name = StringField("Name of the cafe", validators=[DataRequired()])
    map_url = StringField("Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField("Cafe Location", validators=[DataRequired()])
    coffee_price = FloatField("Cafe Price in €", validators=[DataRequired(), NumberRange(min=0)])
    seats = IntegerField('How Many Seats?', validators=[DataRequired(), NumberRange(min=0)])
    has_toilet = BooleanField("Toilets Available?")
    has_wifi = BooleanField("WiFi Available?")
    has_sockets = BooleanField("Sockets Available?")
    can_take_calls = BooleanField("Call taking Available?")
    submit = SubmitField("Add Cafe")


class RegisterForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Sign Me Up!')


class LoginForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Let Me In!')

