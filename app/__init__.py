from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config
from flask_wtf.csrf import generate_csrf
import os

db = SQLAlchemy()
csrf = CSRFProtect()


def inject_csrf_token():
    return dict(csrf_token=lambda: generate_csrf())


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # tạo thư mục instance nếu chưa có
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)
    csrf.init_app(app)

    from app.routes.main import main
    from app.routes.api import api
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
