"""add users table

Revision ID: 9770667ea6ea
Revises: 42f36a972d96
Create Date: 2022-01-17 17:22:05.020525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9770667ea6ea'
down_revision = '42f36a972d96'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
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
    op.drop_table("users")
    pass
