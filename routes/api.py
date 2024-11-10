from flask import url_for, session, Blueprint, current_app, request, jsonify
import os

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


@api_bp.route("/api/upload/audio", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    allowed_extensions = {"wav", "mp3"}
    file_extension = file.filename.rsplit(".", 1)[1].lower()

    if file_extension not in allowed_extensions:
        return jsonify({"error": "Invalid file format. Only .wav and .mp3 are allowed."}), 400

    print(f'file ={file}')

    # Call model #

    return jsonify({"message": "File uploaded successfully!"}), 200

# @api_bp.route("/api/get/phrase", methods=["POST"])
# def return_words(phrase, wrong_words):

