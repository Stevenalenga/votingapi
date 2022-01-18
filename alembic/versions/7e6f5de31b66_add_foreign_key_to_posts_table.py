"""add foreign-key to posts table

Revision ID: 7e6f5de31b66
Revises: 9770667ea6ea
Create Date: 2022-01-17 17:27:50.869721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e6f5de31b66'
down_revision = '9770667ea6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "owner_id", sa.Integer(), nullable=False)),
    op.create_foreign_key("posts_user_fk", source_table="posts", referent_table="users", local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owners_id")
    pass
