from flask import Blueprint, render_template, flash, request
from flask_login import login_required

from app.forms import EmailForm
from app.email import send_email

main = Blueprint('main', __name__)

@main.route('/cv')
@login_required
def cv():
    return render_template('cv.html')

@main.route('/portfolio')
@login_required
def portfolio():
    return render_template('portfolio.html')

@main.route('/email', methods=['GET', 'POST'])
@login_required
def email():
    form = EmailForm(request.form)

    if request.method == 'POST' and form.validate():
        send_email(request.form['companyName'], request.form['message'])
        flash("Your message has been sent")

    return render_template('email.html', form=form)