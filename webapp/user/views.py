from flask import render_template, flash, redirect, url_for,Blueprint
from webapp.user.forms import LoginForm

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)