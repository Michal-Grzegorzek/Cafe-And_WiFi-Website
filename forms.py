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


    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(250), unique=True, nullable=True)
    # map_url = db.Column(db.String(500), nullable=True)
    # img_url = db.Column(db.String(500), nullable=True)
    # location = db.Column(db.String(250), nullable=True)
    # seats = db.Column(db.String(250), nullable=True)
    # has_toilet = db.Column(db.Boolean, nullable=True)
    # has_wifi = db.Column(db.Boolean, nullable=True)
    # has_sockets = db.Column(db.Boolean, nullable=True)
    # can_take_calls = db.Column(db.Boolean, nullable=True)
    # coffee_price = db.Column(db.String(250), nullable=True)

