"""add browser connection details

Revision ID: 0278f42a3bc1
Revises: eddb2673f0d9
Create Date: 2024-01-27 22:41:50.624620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0278f42a3bc1"
down_revision: Union[str, None] = "eddb2673f0d9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "browser_connection_details",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("browser_user", sa.String(), nullable=True),
        sa.Column("serial_number", sa.String(), nullable=True),
        sa.Column("account_id", sa.String(), nullable=True),
        sa.Column("vpn_used", sa.String(), nullable=True),
        sa.Column("vpn_id", sa.String(), nullable=True),
        sa.Column("ip_used", sa.String(), nullable=True),
        sa.Column("ip_country", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_browser_connection_details_id"),
        "browser_connection_details",
        ["id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_browser_connection_details_id"),
        table_name="browser_connection_details",
    )
    op.drop_table("browser_connection_details")
    # ### end Alembic commands ###
