"""create lists table

Revision ID: 5f7db58effe4
Revises: 
Create Date: 2023-08-08 01:36:21.530441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f7db58effe4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "lists",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, index=True),
        sa.Column("description", sa.String, index=True),
        sa.Column("items", sa.JSON),
        sa.Column("is_active", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("lists")
