from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from webapp.model import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.companys.views import blueprint as database_blueprint


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(user_blueprint)
app.register_blueprint(database_blueprint)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Пользователь'}
    return render_template('index.html', title='Home', user=user)
