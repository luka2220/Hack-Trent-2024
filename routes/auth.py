from flask import Blueprint, url_for, session, current_app, redirect
import requests

# Define Blueprint
auth_bp = Blueprint("auth", __name__)


# Routes
@auth_bp.route("/")
def home():
    return {"message": "home route"}, 200


@auth_bp.route("/login")
def login():
    redirect_uri = url_for('auth.login_callback', _external=True)
    return current_app.google.authorize_redirect(redirect_uri)


@auth_bp.route("/login/callback")
def login_callback():
    token = current_app.google.authorize_access_token()
    session['google_oauth_token'] = token

    # print(f"session = {session}")

    user_info = current_app.google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
    session['current_user'] = user_info

    # print(f"User info = {user_info}")

    return 'Logged in as: ' + user_info['email']


@auth_bp.route("/logout")
def logout():
    token = session.get('google_oauth_token')

    if token:
        # Revoke the token on Google's servers
        revocation_url = 'https://oauth2.googleapis.com/revoke'
        requests.post(revocation_url, params={'token': token['access_token']})

    session.pop('google_oauth_token', None)
    # return redirect(url_for('home'))
    return {'message': "logged out"}
