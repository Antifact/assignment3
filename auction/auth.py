from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
#from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///auction.sqlite'
#db.init_app(app)
# comment
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#create a blueprint
bp = Blueprint('auth', __name__)

@bp.route('/login/', methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    error=None
    if(form.validate_on_submit()):
        user_name = form.username.data
        password = form.password.data
        u1 = User.query.filter_by(Username=user_name).first()
#if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
#check the password - notice password hash function
        elif not check_password_hash(u1.Password, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
#all good, redirect to main page
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)
#it comes here when it is a get method
    return render_template('user_form.html', form=form, heading='Login')

@bp.route('/register/', methods=['GET' , 'POST'])
def register():
    form = RegisterForm()
    error=None
    if form.validate_on_submit():
        print('Register form submitted')
#get username, password and email from the form
        uname =form.username.data
        pwd = form.password.data
        email = form.email.data
        pwd_hash = generate_password_hash(pwd)
#create a new user model object
        new_user = User(Username=uname, Password=pwd_hash, Email=email)
        db.session.add(new_user)
        db.session.commit()
        return ''
#commit to the database and redirect to HTML page
    return render_template('user_form.html', form=form, heading='Login')


class User(db.Model):
    __tablename__ = 'Users'
    Username = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)
    Email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    Password = db.Column(db.String(100), unique=True, nullable=False)



# this is the hint for a login function
# @bp.route('/login', methods=['GET', 'POST'])
# def authenticate(): #view function
#     print('In Login View function')
#     login_form = LoginForm()
#     error=None
#     if(login_form.validate_on_submit()==True):
#         user_name = login_form.user_name.data
#         password = login_form.password.data
#         u1 = User.query.filter_by(name=user_name).first()
#         if u1 is None:
#             error='Incorrect user name'
#         elif not check_password_hash(u1.password_hash, password): # takes the hash and password
#             error='Incorrect password'
#         if error is None:
#             login_user(u1)
#             nextp = request.args.get('next') #this gives the url from where the login page was accessed
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=login_form, heading='Login')
