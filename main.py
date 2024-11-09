from flask import Flask

app = Flask(__name__)


# Routes
@app.route("/")
def home():
    return {"message": "home page", "status": 200}


@app.route("/login")
def login():
    return {"message": "login route", "status": 200}


@app.route("/login/callback")
def login_callback():
    return {"message": "login redirect route from google", "status": 200}


@app.route("/logout")
def logout():
    return {"message": "logout route", "status": 200}
