"""add content column to posts table

Revision ID: a44c5e9ae7b5
Revises: ad4d1f64a3fe
Create Date: 2022-01-14 16:08:14.015341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a44c5e9ae7b5'
down_revision = 'ad4d1f64a3fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "content", sa.String(), nullable=False
    ))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
