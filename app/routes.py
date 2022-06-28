# -*- coding: utf-8 -*- 
import profile
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
import requests
import csv

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/upload', methods=['POST'])
def upload():
    request_info = request.files['file']
    

