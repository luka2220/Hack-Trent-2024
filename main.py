# main.py
from flask import Flask
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from config import Config
from extensions import db, migrate
from routes.api import api_bp
from routes.auth import auth_bp
from oauth.google import register_google_oauth
import os

load_dotenv(".env")


def create_app():
    # Initialize the app
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = os.getenv("FLASK_SECRET")
    app.config['SESSION_COOKIE_NAME'] = 'google_oauth_session'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize OAuth
    oauth = OAuth(app)
    app.google = register_google_oauth(oauth)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)

    return app
