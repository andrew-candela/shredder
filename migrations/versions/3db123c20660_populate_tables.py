"""populate tables

Revision ID: 3db123c20660
Revises: 6d906ea92a8d
Create Date: 2024-04-17 08:44:28.051315

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3db123c20660"
down_revision: Union[str, None] = "6d906ea92a8d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

bind = op.get_bind()
session = sa.orm.Sess


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
