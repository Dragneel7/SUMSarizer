"""empty message

Revision ID: a4f3c426417e
Revises: 46ae5e506646
Create Date: 2016-07-01 06:25:23.060945

"""

# revision identifiers, used by Alembic.
revision = 'a4f3c426417e'
down_revision = '46ae5e506646'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'stormpath_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('stormpath_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
