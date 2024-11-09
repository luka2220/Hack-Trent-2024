# Hack-Trent-2024

## Server Docs

***

### Running the server

- python -m .venv
- source .venv/bin/activate
- python -m pip install -r requirements.txt
- create the .env file

### Performing database operations

- *(Create a migration repo)*: flask --app main.py db init
- *(Create a db migration)*: flask --app main.py db migrate -m "users table"
- *(Apply the migration changes to the db)*: flask --app main.py db upgrade
