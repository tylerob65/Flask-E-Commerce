from app.models import db, Users
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate
from app.auth.auth_routes import auth

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


login_manager.login_view = 'auth.loginPage'

app.register_blueprint(auth)

from . import routes
from . import models