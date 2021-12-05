"""create politicians table

Revision ID: 587cd3f0b770
Revises:
Create Date: 2021-12-04 10:57:50.059937

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "587cd3f0b770"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "politicians",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("state", sa.String(50)),
    )


def downgrade():
    op.drop_table("politicians")
