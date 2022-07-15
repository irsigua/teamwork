from flask import render_template, request,Blueprint
import csv


blueprint = Blueprint('load', __name__, url_prefix='/loadfile')


@blueprint.route('/load', methods=['POST'])

def get_csv():
    request_info = request.files['file']
    f = request_info.readlines()
    print(f)
    return render_template('load.html')

