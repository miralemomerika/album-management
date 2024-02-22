"""on delete set to null

Revision ID: 04a34165339f
Revises: b6128982a01f
Create Date: 2024-01-31 15:10:16.804168

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "04a34165339f"
down_revision: Union[str, None] = "b6128982a01f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "albums_music_services_id_fkey", "albums", type_="foreignkey"
    )
    op.drop_constraint(
        "albums_distributor_id_fkey", "albums", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "albums",
        "music_services",
        ["music_services_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        None,
        "albums",
        "distributors",
        ["distributor_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_constraint(
        "distributors_browser_details_id_fkey",
        "distributors",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "distributors",
        "browser_connection_details",
        ["browser_details_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_constraint(
        "music_services_user_id_fkey", "music_services", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "music_services",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_constraint(
        "payment_informations_user_id_fkey",
        "payment_informations",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "payment_informations",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_constraint("songs_album_id_fkey", "songs", type_="foreignkey")
    op.create_foreign_key(
        None, "songs", "albums", ["album_id"], ["id"], ondelete="SET NULL"
    )
    op.drop_constraint(
        "user_statuses_user_id_fkey", "user_statuses", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "user_statuses",
        "users",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "user_statuses", type_="foreignkey")
    op.create_foreign_key(
        "user_statuses_user_id_fkey",
        "user_statuses",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(None, "songs", type_="foreignkey")
    op.create_foreign_key(
        "songs_album_id_fkey", "songs", "albums", ["album_id"], ["id"]
    )
    op.drop_constraint(None, "payment_informations", type_="foreignkey")
    op.create_foreign_key(
        "payment_informations_user_id_fkey",
        "payment_informations",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(None, "music_services", type_="foreignkey")
    op.create_foreign_key(
        "music_services_user_id_fkey",
        "music_services",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(None, "distributors", type_="foreignkey")
    op.create_foreign_key(
        "distributors_browser_details_id_fkey",
        "distributors",
        "browser_connection_details",
        ["browser_details_id"],
        ["id"],
    )
    op.drop_constraint(None, "albums", type_="foreignkey")
    op.drop_constraint(None, "albums", type_="foreignkey")
    op.create_foreign_key(
        "albums_distributor_id_fkey",
        "albums",
        "distributors",
        ["distributor_id"],
        ["id"],
    )
    op.create_foreign_key(
        "albums_music_services_id_fkey",
        "albums",
        "music_services",
        ["music_services_id"],
        ["id"],
    )
    # ### end Alembic commands ###