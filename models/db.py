import sqlalchemy as sa
import sqlalchemy.orm as so
from main import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    profile_picture: so.Mapped[str] = so.mapped_column(sa.string(120), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
