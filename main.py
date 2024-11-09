from flask import Flask, url_for
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
import os

# Load all environment variables
load_dotenv(".env")
FLASK_SECRET = os.getenv("FLASK_SECRET")
GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_SECRET = os.getenv("GOOGLE_OAUTH_SECRET")
app = Flask(__name__)
app.secret_key = FLASK_SECRET

# Initialize google oauth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=GOOGLE_OAUTH_CLIENT_ID,
    client_secret=GOOGLE_OAUTH_SECRET,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    client_kwargs={'scope': 'openid profile email'}
)


# Routes
@app.route("/")
def home():
    return {"message": "home route", "status": 200}


@app.route("/login")
def login():
    redirect_uri = url_for('login_callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/login/callback")
def login_callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    return 'Logged in as: ' + user_info['email']


@app.route("/logout")
def logout():
    return {"message": "logout route", "status": 200}
