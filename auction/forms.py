
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired()])
    email = StringField("Email ID", validators=[InputRequired(),Email("Please enter a valid email")])
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired()])            
    confirm = PasswordField("Confirm Password" , validators=[ EqualTo('confirm', message="Passwords should match")])
    #submit button
    submit = SubmitField("Register")