"""add content column to posts table

Revision ID: 630d23512c74
Revises: 6355047f52af
Create Date: 2025-09-27 13:49:09.348352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '630d23512c74'
down_revision: Union[str, Sequence[str], None] = '6355047f52af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
