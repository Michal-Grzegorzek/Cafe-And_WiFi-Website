from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# #WTForm

class Cafe(FlaskForm):
    name = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
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

