from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from ds_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from ds_blog.users.routes import users
from ds_blog.posts.routes import posts
from ds_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

def create_app(config_class=Config):
    app = Flask(__name__)
    aap.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from ds_blog.users.routes import users
    from ds_blog.posts.routes import posts
    from ds_blog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
