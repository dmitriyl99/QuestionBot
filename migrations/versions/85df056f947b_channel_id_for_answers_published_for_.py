"""Channel id for answers, published for tests

Revision ID: 85df056f947b
Revises: 11ddea564d92
Create Date: 2019-06-02 23:28:17.637917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85df056f947b'
down_revision = '11ddea564d92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('channel_id', sa.Integer(), nullable=True))
    op.add_column('test', sa.Column('published', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'published')
    op.drop_column('answer', 'channel_id')
    # ### end Alembic commands ###
