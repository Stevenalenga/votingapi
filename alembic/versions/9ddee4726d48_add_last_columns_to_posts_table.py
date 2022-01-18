"""add last columns to posts table

Revision ID: 9ddee4726d48
Revises: 7e6f5de31b66
Create Date: 2022-01-17 18:18:55.673435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ddee4726d48'
down_revision = '7e6f5de31b66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="True")),
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")
    )),
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")

    pass
