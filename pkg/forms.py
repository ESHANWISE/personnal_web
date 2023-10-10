from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,SelectField
from wtforms.validators import Email,DataRequired,EqualTo,Length

class RegForm(FlaskForm):
    fname = StringField("FirstName",validators=[DataRequired(message="FirstName is too short")])
    lname = StringField("LastName",validators=[Length(min=5, message="Last name is not Biafra")])
    usermail = StringField("Emial",validators=[Email(message="Invalid Email"), DataRequired(message="Email must be supplied"),Length(min=7,message="Email is too short")])
    pwd = PasswordField("Enter Password",validators=[DataRequired()])
    cpwd = PasswordField("Confirm Password",validators=[EqualTo('pwd',message="The two passwords must match")])
    profile = TextAreaField("Your Profile")
    btnsubmit = SubmitField("Register!")
    