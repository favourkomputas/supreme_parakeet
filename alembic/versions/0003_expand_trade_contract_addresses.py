"""Allow full token contract addresses in trades.

Revision ID: 0003
Revises: 0002
Create Date: 2026-08-07
"""

from typing import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0003"
down_revision: str | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column(
        "trades", "asset_in", existing_type=sa.String(length=32), type_=sa.String(255)
    )
    op.alter_column(
        "trades", "asset_out", existing_type=sa.String(length=32), type_=sa.String(255)
    )


def downgrade() -> None:
    op.alter_column(
        "trades", "asset_out", existing_type=sa.String(length=255), type_=sa.String(32)
    )
    op.alter_column(
        "trades", "asset_in", existing_type=sa.String(length=255), type_=sa.String(32)
    )
