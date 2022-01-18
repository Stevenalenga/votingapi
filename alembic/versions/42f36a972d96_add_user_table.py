"""add user table

Revision ID: 42f36a972d96
Revises: a44c5e9ae7b5
Create Date: 2022-01-17 16:38:40.540605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f36a972d96'
down_revision = 'a44c5e9ae7b5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("user",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )

    pass


def downgrade():
    op.drop_table("user")
    pass
