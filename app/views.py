from flask import render_template, flash, redirect, url_for, abort, request, session
from app import app
from app.models import User
from .forms import LoginForm
from flask.ext.login import login_user , logout_user , current_user , login_required
from sqlalchemy import func

@app.route('/')
def index():
    title = 'Miguel'
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter(func.lower(User.username) == func.lower(username)).first()
        if login_user(user, remember_me):
            flash("You were logged in.", "success")
            return redirect(request.args.get("next") or url_for('index'))
        else:
            flash("Login failed, user not validated", "error")
            return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for('index')) 


@app.route("/settings")
@login_required
def settings():
    return 'Secret View'



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
