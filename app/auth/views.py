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
    




