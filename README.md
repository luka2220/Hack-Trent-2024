# Hack-Trent-2024

## Server Docs

***

### Running the server

- python -m .venv
- source .venv/bin/activate
- python -m pip install -r requirements.txt
- create the .env file
- gunicorn --reload -w 4 -b 127.0.0.1:8000 "main:create_app()"

### Performing database operations

- *(Create a migration repo)*: flask --app main:create_app db init
- *(Create a db migration)*: flask --app main:create_app db migrate -m "users table"
- *(Apply the migration changes to the db)*: flask --app main:create_app db upgrade
