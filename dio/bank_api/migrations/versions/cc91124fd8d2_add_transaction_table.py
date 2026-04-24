"""Add transaction table

Revision ID: cc91124fd8d2
Revises: 092da3817649
Create Date: 2026-04-24 11:13:29.921631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc91124fd8d2'
down_revision: Union[str, Sequence[str], None] = '092da3817649'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
