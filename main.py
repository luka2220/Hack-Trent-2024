from flask import Flask
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from routes.api import api_bp
from routes.auth import auth_bp
from oauth.google import register_google_oauth
from config import Config

# Load all environment variables
load_dotenv(".env")
FLASK_SECRET = os.getenv("FLASK_SECRET")
app = Flask(__name__)
app.secret_key = FLASK_SECRET
app.config['SESSION_COOKIE_NAME'] = 'google_oauth_session'
app.config.from_object(Config)

# Initialize DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register oauth
oauth = OAuth(app)
app.google = register_google_oauth(oauth)

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
