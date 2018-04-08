"""empty message

Revision ID: bfb957b7f1ed
Revises: 91d6e13006cc
Create Date: 2018-04-08 17:08:17.846359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb957b7f1ed'
down_revision = '91d6e13006cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('disk_type', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server', 'disk_type')
    # ### end Alembic commands ###
