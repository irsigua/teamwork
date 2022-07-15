import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename,SharedDataMiddleware
from flask import send_from_directory


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('load.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

app.add_url_rule('/uploads/<filename>', 'uploaded_file',build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/uploads':  app.config['UPLOAD_FOLDER']})