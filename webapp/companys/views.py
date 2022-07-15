from flask import render_template, flash, redirect, url_for,Blueprint
from webapp.companys.models import Company,Direction,Payments

blueprint = Blueprint('database', __name__, url_prefix='/database')

@blueprint.route('/data',methods = ['GET'])
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
    return render_template('data.html',companys=companys)