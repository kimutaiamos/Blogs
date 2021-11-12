from flask import render_template, redirect, url_for, request , flash
from flask_login import login_user, login_required, logout_user
from .forms import RegistrationForm, loginForm
from .import auth
from ..import db
from ..models import User



#registration route
@auth.route('templates/auth/reqister', methods=['GET','POST'])
def register():
    """
    function that registers the users
    """

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, passwird = form.Password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    title = "registration"

    return render_template('auth/register.html', RegistrationForm = form, title = title)



#logging in function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    function that checks if the form is validated
    """

    login_form = loginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))


            flash('Invalid Username or password')

    title = "blogs"
    return render_template('auth/login.html',login_form = login_form, title = title)
    





