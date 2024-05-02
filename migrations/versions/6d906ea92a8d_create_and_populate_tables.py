"""create and populate tables

Revision ID: 6d906ea92a8d
Revises: 
Create Date: 2024-04-14 10:21:14.745337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d906ea92a8d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String),
    )
    op.create_table(
        "linker",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("link", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("link_ref", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True, unique=True),
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("link_ref", sa.Integer, sa.ForeignKey("linker.link_ref"), nullable=False, index=True),
    )
    op.create_table(
        "referrals",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("referrer", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("referree", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("link_id", sa.Integer, sa.ForeignKey("linker.id"), nullable=False, index=True),
        sa.Column("order_id", sa.Integer, sa.ForeignKey("orders.id"), nullable=False, index=True),
    )
    # op.bulk_insert()




def downgrade() -> None:
    op.drop_table("users")
