"""Align schema with ModelTable including compiled_sql and upstream models

Revision ID: cbb70bad3492
Revises: 9ea4f5d4b0a1
Create Date: 2025-04-02 16:02:30.922364

"""
from typing import Sequence, Union
import logging

from alembic import op
import sqlalchemy as sa


from dbt_llm_agent.utils.logging import get_logger

# Get logger
logger = get_logger("alembic.migration")

# revision identifiers, used by Alembic.
revision: str = "cbb70bad3492"
down_revision: Union[str, None] = "9ea4f5d4b0a1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    logger.info(
        f"Starting Align schema with ModelTable including compiled_sql and upstream models upgrade"
    )

    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

    logger.info(
        f"Completed Align schema with ModelTable including compiled_sql and upstream models upgrade"
    )


def downgrade() -> None:
    """Downgrade schema."""
    logger.info(
        f"Starting Align schema with ModelTable including compiled_sql and upstream models downgrade"
    )

    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

    logger.info(
        f"Completed Align schema with ModelTable including compiled_sql and upstream models downgrade"
    )
