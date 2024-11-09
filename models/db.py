import sqlalchemy as sa
from sqlalchemy.dialects.sqlite import JSON
from extensions import db


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(120), index=True, unique=True)
    name = sa.Column(sa.String(120), index=True)
    profile_picture = sa.Column(sa.String(120), index=True)
    languages = db.Column(JSON)

    def __repr__(self):
        return f'<User {self.name}>'
