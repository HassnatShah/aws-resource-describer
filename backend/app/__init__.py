# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_cors import CORS
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Cache
    cache.init_app(app, config={'CACHE_TYPE': 'SimpleCache'})

    # Register Blueprints
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app