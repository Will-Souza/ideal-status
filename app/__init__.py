from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config


db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from app.models import Users

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

from app.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)
