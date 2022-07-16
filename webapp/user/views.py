from flask import render_template, flash, redirect, url_for,Blueprint
from flask_login import login_user,logout_user,current_user,LoginManager
from webapp.user.forms import LoginForm
from webapp.user.models import User
blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title = title, form=login_form)

@blueprint.route('/process-login',methods = ['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=form.remember_me.data)
            flash("Вы успешно вошли на сайт")
            return redirect(url_for('index'))
        flash('Неправельное имя или пароль')
        return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно залогинились')
    return redirect(url_for('index'))  