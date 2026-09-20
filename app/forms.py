from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, BooleanField, PasswordField, validators

class EmailForm(Form):
    companyName = StringField('Company Name', validators=[validators.DataRequired()])
    message = TextAreaField('Message', validators=[validators.DataRequired()])

# Switched to FlaskForm for login due to CSRF protection against cross-site request-forgery
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators= [validators.DataRequired()])
    account = BooleanField()