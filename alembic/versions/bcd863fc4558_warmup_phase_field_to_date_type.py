"""warmup phase field to date type

Revision ID: bcd863fc4558
Revises: 04a34165339f
Create Date: 2024-02-12 14:06:38.741497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bcd863fc4558"
down_revision: Union[str, None] = "04a34165339f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # First, update non-convertible or specific VARCHAR values to NULL
    # With this we set all existing non-NULL VARCHAR values to NULL
    op.execute(
        "UPDATE users SET warmup_phase_until = NULL WHERE warmup_phase_until IS NOT NULL"
    )

    # Then, alter the column type to DATE
    op.execute(
        "ALTER TABLE users ALTER COLUMN warmup_phase_until TYPE DATE USING warmup_phase_until::DATE"
    )


def downgrade() -> None:
    # Alter the column back to VARCHAR without attempting to restore original values
    op.execute(
        "ALTER TABLE users ALTER COLUMN warmup_phase_until TYPE VARCHAR"
    )
