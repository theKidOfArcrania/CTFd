"""add user and team secrets

Revision ID: d2ea78f95c1e
Revises: 080d29b15cd3
Create Date: 2019-11-05 23:34:21.858587

"""
from alembic import op
import sqlalchemy as sa
import os

# revision identifiers, used by Alembic.
revision = 'd2ea78f95c1e'
down_revision = '080d29b15cd3'
branch_labels = None
depends_on = None


def upgrade():
    from CTFd.models import db, Teams, Users
    from CTFd.utils.encoding import hexencode
    for u in Users.query.filter_by(secret=None).all():
        u.secret = hexencode(os.urandom(32))
    for t in Teams.query.filter_by(secret=None).all():
        t.secret = hexencode(os.urandom(32))
    db.session.commit()


def downgrade():
    from CTFd.models import db, Teams, Users
    for u in Users.query.all():
        u.secret = None
    for t in Teams.query.all():
        t.secret = None
    db.session.commit()
