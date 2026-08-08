"""add discovery models

Revision ID: cdb78faeab49
Revises: 60279c668db8
Create Date: 2026-07-27 19:56:03.840861
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "cdb78faeab49"
down_revision: Union[str, Sequence[str], None] = "60279c668db8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "discovery_scans",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("network", sa.String(length=100), nullable=False),
        sa.Column(
            "scan_type",
            sa.Enum("NMAP", "MANUAL", "AGENT", name="scantype"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "RUNNING",
                "COMPLETED",
                "FAILED",
                name="discoverystatus",
            ),
            nullable=False,
        ),
        sa.Column("hosts_found", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "asset_observations",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("scan_id", sa.UUID(), nullable=False),
        sa.Column("asset_id", sa.UUID(), nullable=True),
        sa.Column("ip_address", sa.String(length=45), nullable=False),
        sa.Column("mac_address", sa.String(length=17), nullable=True),
        sa.Column("hostname", sa.String(length=255), nullable=True),
        sa.Column("operating_system", sa.String(length=255), nullable=True),
        sa.Column("vendor", sa.String(length=255), nullable=True),
        sa.Column(
            "source",
            sa.Enum(
                "NMAP",
                "MANUAL",
                "SNMP",
                "AGENT",
                name="discoverysource",
            ),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.Enum(
                "NEW",
                "MATCHED",
                "APPROVED",
                "REJECTED",
                name="observationstatus",
            ),
            nullable=False,
        ),
        sa.Column("confidence_score", sa.Integer(), nullable=False),
        sa.Column(
            "ports",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "raw_scan_data",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "observed_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["assets.id"],
        ),
        sa.ForeignKeyConstraint(
            ["scan_id"],
            ["discovery_scans.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Indexes for fast lookups
    op.create_index(
        "ix_asset_observations_ip_address",
        "asset_observations",
        ["ip_address"],
    )

    op.create_index(
        "ix_asset_observations_scan_id",
        "asset_observations",
        ["scan_id"],
    )

    op.create_index(
        "ix_asset_observations_asset_id",
        "asset_observations",
        ["asset_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index("ix_asset_observations_asset_id")
    op.drop_index("ix_asset_observations_scan_id")
    op.drop_index("ix_asset_observations_ip_address")

    op.drop_table("asset_observations")
    op.drop_table("discovery_scans")