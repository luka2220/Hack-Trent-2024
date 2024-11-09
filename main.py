from flask import Flask, url_for, session, redirect
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
import os
import requests

# Load all environment variables
load_dotenv(".env")
FLASK_SECRET = os.getenv("FLASK_SECRET")
GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_SECRET = os.getenv("GOOGLE_OAUTH_SECRET")
app = Flask(__name__)
app.secret_key = FLASK_SECRET
app.config['SESSION_COOKIE_NAME'] = 'google_oauth_session'

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
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid profile email', 'response_type': 'code',
                   'redirect_uri': 'http://127.0.0.1:8000/login/callback'},
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs"
)


# Routes
@app.route("/")
def home():
    return {"message": "home route"}, 200


@app.route("/login")
def login():
    redirect_uri = url_for('login_callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/login/callback")
def login_callback():
    token = google.authorize_access_token()
    session['google_oauth_token'] = token

    print(f"session = {session}")

    user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
    return 'Logged in as: ' + user_info['email']


@app.route("/logout")
def logout():
    token = session.get('google_oauth_token')

    if token:
        # Revoke the token on Google's servers
        revocation_url = 'https://oauth2.googleapis.com/revoke'
        requests.post(revocation_url, params={'token': token['access_token']})

    session.pop('google_oauth_token', None)
    # return redirect(url_for('home'))
    return {'message': "logged out"}


@app.route("/api/user/current")
def get_current_user():
    token = session.get('google_oauth_token')

    print(f"session token = {token}")

    if token:
        print(f"access_token ===== {token["access_token"]}")
        
        current_user = google.get('https://www.googleapis.com/oauth2/v3/userinfo',
                                  headers={'Authorization': f'Bearer {token["access_token"]}'}).json()
        return {"current user info": current_user}, 200

    return {"Unauthorized": "No user is currently signed in"}, 401


if __name__ == "__main__":
    app.run(debug=True)
