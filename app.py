# Import
from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators
import boto3
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


# Adapted this for AWS emails -> https://qxf2.com/blog/sending-email-through-amazon-ses-with-flask-app/
class EmailForm(Form):
    message = TextAreaField('Message', validators=[validators.DataRequired()])

@app.route('/email', methods=['GET', 'POST'])
def email():
    # Takes the form data
    form = EmailForm(request.form)

    # AWS client object
    ses_client = boto3.client('ses')


    # TODO: Make it so they have to put in their email (need to complete production access form)
    # Checks if someone is sending an email
    if request.method == 'POST' and form.validate():
        emailAddress = "cabbagedevops@gmail.com"
        subject = "NEW JOB OFFER"
        message = request.form['message']

        emailData = {}
        emailData['email'] = emailAddress
        emailData['message'] = message

        emailHTML = render_template('email.html', emailData=emailData)

        # Sending the email in two forms HTML and raw text (incase the mail provider cant handle HTML)
        response = ses_client.send_email(
            Destination = { 'ToAddresses': [emailAddress] },
            Message = { 'Subject': {'Charset': 'UTF-8', 'Data': subject.encode('utf-8') },
                        'Body': { 'Html': {'Charset': 'UTF-8', 'Data': emailHTML.encode('utf-8')},
                                  'Text': {'Charset': 'UTF-8', 'Data': message.encode('utf-8')} },},
            Source= emailAddress,
        )




        flash("Your message has been sent")

    return render_template('email.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)