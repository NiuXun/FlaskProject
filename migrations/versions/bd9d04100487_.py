"""empty message

Revision ID: bd9d04100487
Revises: 634a4e09cdae
Create Date: 2018-04-03 16:05:10.953917

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd9d04100487'
down_revision = '634a4e09cdae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device_model', sa.Column('device_type', sa.String(length=64), nullable=True))
    op.alter_column('vendor', 'name',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vendor', 'name',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.drop_column('device_model', 'device_type')
    # ### end Alembic commands ###