"""Update User_Game table to just have time instead of start + end time

Revision ID: 3a530fc4b69f
Revises: 3c501b7574ab
Create Date: 2023-07-19 15:39:45.568247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a530fc4b69f'
down_revision = '3c501b7574ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.Integer(), nullable=True))
        batch_op.drop_column('end_time')
        batch_op.drop_column('start_time')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_time', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('end_time', sa.INTEGER(), nullable=True))
        batch_op.drop_column('time')

    # ### end Alembic commands ###
