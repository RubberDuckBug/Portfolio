import boto3
from flask import render_template

def send_email(company_name, message):
    ses_client = boto3.client('ses')

    email_address = "cabbagedevops@gmail.com"
    subject = "NEW JOB OFFER - " + company_name

    email_data = {}
    email_data['email'] = email_address
    email_data['message'] = message

    email_html = render_template('email_template.html', emailData=email_data)

    response = ses_client.send_email(
        Destination={'ToAddresses': [email_address]},
        Message={
            'Subject': {'Charset': 'UTF-8', 'Data': subject},
            'Body': {
                'Html': {'Charset': 'UTF-8', 'Data': email_html},
                'Text': {'Charset': 'UTF-8', 'Data': message}
            },
        },
        Source=email_address,
    )

    return response