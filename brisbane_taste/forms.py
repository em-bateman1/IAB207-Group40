from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange

# creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm): #NEED MIN AND MAX CHARACTER LIMITS
    full_name = StringField("Full Name", validators=[InputRequired()])
    user_name = StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[InputRequired(), Email("Please enter a valid email")])
    street_address = TextAreaField("Street Address", validators=[InputRequired()])
    phone = StringField("Mobile Phone", validators=[InputRequired()]) #CUSTOM VALIDATOR FOR PHONE NUMBER FORMAT REQUIRED
    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")]) #need to add password constraints (min&max lengths, required characters)
    confirm = PasswordField("Confirm Password", validators=[InputRequired()])

    # submit button
    submit = SubmitField("Register")