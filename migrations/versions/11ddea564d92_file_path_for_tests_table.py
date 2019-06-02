"""File path for tests table

Revision ID: 11ddea564d92
Revises: de14a0441ce0
Create Date: 2019-06-02 21:31:55.291135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ddea564d92'
down_revision = 'de14a0441ce0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('file_path', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'file_path')
    # ### end Alembic commands ###
