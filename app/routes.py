# -*- coding: utf-8 -*- 
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import Company

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ираклий'}
    return render_template('index.html', title='Home', user=user)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/data',methods = ['GET'])
def data():
    companys = Company.query.order_by(Company.inn).all()
    companys_dict={}
    for company in companys:
        companys_dict['inn'] = company.inn
        companys_dict['name'] = company.name
    return render_template('data.html',companys=companys)