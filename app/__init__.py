from flask import Flask

import settings
from app.view import user_bp
from exts import db, api


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app=app)
    api.init_app(app=app)
    app.register_blueprint(user_bp)
    return app
