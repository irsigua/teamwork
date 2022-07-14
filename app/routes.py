# -*- coding: utf-8 -*- 
import profile
from unittest import result
from flask import render_template, flash, redirect, url_for, request, Blueprint
import sqlalchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
import csv

class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')
csv_bp = Blueprint('csv_bp', __name__)

@csv_bp.route('/')
@csv_bp.route('/index')
def index():
    user = {'username': 'User'}
    return render_template('index.html', title='Home', user=user)


@csv_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@csv_bp.route('/get_csv', methods=['POST'])
def get_csv():
    request_info = request.files['file']
    f = request_info.readlines()
    print(f)
    return {'ответ': 'все ок'}
    

