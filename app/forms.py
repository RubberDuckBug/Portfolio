from wtforms import Form, StringField, TextAreaField, validators

class EmailForm(Form):
    companyName = StringField('Company Name', validators=[validators.DataRequired()])
    message = TextAreaField('Message', validators=[validators.DataRequired()])