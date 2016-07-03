"""empty message

Revision ID: 8ac91a55e860
Revises: a4f3c426417e
Create Date: 2016-07-03 01:39:07.556177

"""

# revision identifiers, used by Alembic.
revision = '8ac91a55e860'
down_revision = 'a4f3c426417e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sz_job', sa.Column('archived', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sz_job', 'archived')
    ### end Alembic commands ###