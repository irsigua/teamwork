# -*- coding: utf-8 -*- 
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import Company, Direction

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
    companys = Company.query.join(Direction,Company.inn==Direction.company_inn).with_entities(Company.inn,Company.name,Direction.set_number,Direction.payer,Direction.recipient).all()
    companys_list = []
    for inn, name, set_number, payer, recipient in companys:
        companys_dict={}
        companys_dict['inn'] = inn
        companys_dict['name'] = name
        companys_dict['set_number'] = set_number
        companys_dict['payer'] = payer
        companys_dict['recipient'] = recipient
        companys_list.append(companys_dict)
    print(companys_list)          
    # return render_template('data.html',companys=companys)
    return None
