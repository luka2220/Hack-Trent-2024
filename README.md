# Hack-Trent-2024

## Server Documentation

***

* The server code lives in the root directory with the main entry point in main.py
* It is a flask application with a sqlite database named hacktrent.db in `./db`
* The server's development environment is in a docker container as well, defined in the Dockerfile

### Running the server with a python virtual environment

* NOTE: Make sure python is installed on your system

*Mac/Linux Setup*

- `python -m .venv`
- `source .venv/bin/activate`
- `python -m pip install -r requirements.txt`
- `create the .env file with secrets`
- `gunicorn --reload -w 4 -b 127.0.0.1:8000 "main:create_app()"`

*Windows Setup*

- `python -m venv .venv`
- `.\.venv\Scripts\activate`
- `pip install requirements.txt`
- `create the .env file with secrets`
- `waitress-serve --host=127.0.0.1 --port=8001 main:app`

### Running the server with docker

* NOTE: Make sure docker is installed on your system

*Run the Server Container*

- `docker build -t server-image .`
- `docker run -d -p 8001:8000 -v /db/hacktrent.db --name hack-trent-server-app server-image`

*Run the Model Container*

### Performing database operations (if needed)

- *(Create a migration repo)*: flask --app main:create_app db init
- *(Create a db migration)*: flask --app main:create_app db migrate -m "users table"
- *(Apply the migration changes to the db)*: flask --app main:create_app db upgrade

## Client Documentation

***

* The client code lives inside the client directory
* With the server code running open another terminal session to get started

### Running the client

- In the root directory: `cd client`
- `npm i`
- `npm run dev`