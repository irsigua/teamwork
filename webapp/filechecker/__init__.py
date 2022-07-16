import os
from flask import Flask, flash,render_template, request,redirect, url_for, abort
from werkzeug.utils import secure_filename



app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['csv']
app.config['UPLOAD_PATH'] = 'uploads'





@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    flash('файл успешно загружен')
    