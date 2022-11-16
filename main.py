import werkzeug
from functools import wraps
from flask import g, request, redirect, url_for
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
import os
from forms import Cafe


app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'any secret string'
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)

# login_manager = LoginManager()
# login_manager.init_app(app)


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///cafes.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLES

class AllCafes(db.Model):
    __tablename__ = "all_cafes"
    id = db.Column(db.Integer, primary_key=True)
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # author = relationship("User", back_populates="posts")
    name = db.Column(db.String(250), unique=True, nullable=True)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)


# db.create_all()

@app.route('/')
def home():
    form = Cafe()
    return render_template("index.html", form=form)


@app.route("/add-cafe", methods=["POST", "GET"])
def add_new_cafe():
    form = Cafe()
    print("1")
    if form.validate_on_submit():
        print("3")
        new_cafe = AllCafes(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            can_take_calls=form.can_take_calls.data,
            coffee_price=form.coffee_price.data,
            # date=date.today().strftime("%B %d, %Y")
        )

        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add-cafe.html", form=form)








# @app.route("/about")
# def about():
#     return render_template("about.html", logged_in=current_user.is_authenticated)
#
#
# @app.route("/contact")
# def contact():
#     return render_template("contact.html", logged_in=current_user.is_authenticated)



if __name__ == "__main__":
    app.run(debug=True)

