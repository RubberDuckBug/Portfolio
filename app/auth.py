from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user
from app.forms import LoginForm, EmailForm
from app.models import Employer, Candidate
from app.utils import url_has_allowed_host_scheme
from app.email import send_email
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__)
main = Blueprint('main', __name__)

@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        isEmployer = form.account.data

        # Checks if there is a user in the database and takes the first instance of it
        if isEmployer:
            user = Employer.query.filter_by(username=form.username.data).first()
        else:
            user = Candidate.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)

            # This is if the users are not signed in and try to access an auth page
            # It will send them back to the login page
            next = request.args.get('next')
            if not url_has_allowed_host_scheme(next, request.host):
                return abort(400)

            return redirect(next or url_for('main.cv'))
        else:
            flash('Invalid username and/or password.')

    return render_template('index.html', form=form)
