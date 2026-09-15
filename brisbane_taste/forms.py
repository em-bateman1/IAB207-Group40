from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

# creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    #need to add missing information also required: street address, phone number, name
    user_name=StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    # linking two fields - password should be equal to data entered in confirm
    street_address = TextAreaField("Street Address", validators=[InputRequired()])
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")]) #need to add password constraints (min&max lengths, required characters)
    confirm = PasswordField("Confirm Password", validators=[InputRequired()])

    # submit button
    submit = SubmitField("Register")