from flask import Blueprint, url_for, session, current_app, redirect
import requests

from extensions import db
from models.db import User

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

    email = user_info.get("email")
    name = user_info.get("name")
    profile_picture = user_info.get("picture")

    # Check if the user exists in the database
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(
            email=email,
            name=name,
            profile_picture=profile_picture
        )
        db.session.add(user)
        db.session.commit()
        print(f'New user created: \n\tEmail: {user.email} \n\tName: {user.name}')

    session["user_id"] = user.id

    redirect_uri = url_for("auth.home", _external=True)
    return redirect(redirect_uri)


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
