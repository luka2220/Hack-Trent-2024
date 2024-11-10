from flask import Flask, redirect, url_for
from flask_oauthlib.client import OAuth
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app and OAuth
app = Flask(__name__)
app.secret_key = os.urandom(24)
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    consumer_secret=os.getenv("GOOGLE_OAUTH_SECRET"),
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)



