"""update table relationships

Revision ID: 33e5df737cd2
Revises: 470a68bb9ea8
Create Date: 2024-08-26 16:38:27.802743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33e5df737cd2'
down_revision: Union[str, None] = '470a68bb9ea8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('category_id', sa.Integer(), nullable=False))
    op.drop_constraint('tasks_user_id_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'categories', ['category_id'], ['id'])
    op.drop_column('tasks', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_user_id_fkey', 'tasks', 'categories', ['user_id'], ['id'])
    op.drop_column('tasks', 'category_id')
    # ### end Alembic commands ###