# Hack-Trent-2024

## Server Docs

***

### Running the server

- python -m .venv
- source .venv/bin/activate
- python -m pip install -r requirements.txt
- create the .env file
- gunicorn --reload -w 4 -b 127.0.0.1:8000 "main:create_app()"

### Running the server with docker

- `docker build -t server-image .`
- `docker run -d -p 8001:8000 -v /db/hacktrent.db --name hack-trent-server-app server-image`

### Performing database operations

- *(Create a migration repo)*: flask --app main:create_app db init
- *(Create a db migration)*: flask --app main:create_app db migrate -m "users table"
- *(Apply the migration changes to the db)*: flask --app main:create_app db upgrade
