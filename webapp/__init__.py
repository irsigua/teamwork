from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from webapp.model import db
from webapp.user.views import blueprint as user_blueprint
from webapp.companys.views import blueprint as database_blueprint
from webapp.filechecker.views import blueprint as load_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_blueprint)
app.register_blueprint(database_blueprint)
app.register_blueprint(load_blueprint)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ираклий'}
    return render_template('index.html', title='Home', user=user)
