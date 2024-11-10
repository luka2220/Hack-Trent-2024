import os

def register_google_oauth(oauth):
    google_oauth_client_id = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
    google_oauth_secret = os.getenv("GOOGLE_OAUTH_SECRET")

    return oauth.register(
        name='google',
        client_id=google_oauth_client_id,
        client_secret=google_oauth_secret,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
        client_kwargs={'scope': 'openid profile email', 'response_type': 'code',
                       'redirect_uri': 'http://127.0.0.1:8001/login/callback'},
        jwks_uri="https://www.googleapis.com/oauth2/v3/certs"
    )



