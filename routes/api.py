from flask import url_for, session, Blueprint, current_app, redirect

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/user/current")
def get_current_user():
    token = session.get('google_oauth_token')
    # print(f"Session token: {token}")

    if token and token.get("access_token"):
        access_token = token["access_token"]
        # print(f"Using access token: {access_token}")

        response = current_app.google.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            token={"access_token": access_token}
        )

        if response.ok:
            current_user = response.json()
            return {"current user info": current_user}, 200
        else:
            # print("Error retrieving user info:", response.text)
            return {"Error": "Failed to retrieve user info"}, 400

    return {"Unauthorized": "No user is currently signed in"}, 401
