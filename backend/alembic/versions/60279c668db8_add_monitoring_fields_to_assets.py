"""add monitoring fields to assets

Revision ID: 60279c668db8
Revises: f20039886852
Create Date: 2026-07-27 15:36:42.827691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60279c668db8'
down_revision: Union[str, Sequence[str], None] = 'f20039886852'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "assets",
        sa.Column("last_seen", sa.DateTime(timezone=True), nullable=True),
    )

    op.add_column(
        "assets",
        sa.Column("risk_score", sa.Integer(), nullable=False, server_default="0"),
    )

    op.add_column(
        "assets",
        sa.Column("is_monitored", sa.Boolean(), nullable=False, server_default="true"),
    )


def downgrade() -> None:
    op.drop_column("assets", "is_monitored")
    op.drop_column("assets", "risk_score")
    op.drop_column("assets", "last_seen")
