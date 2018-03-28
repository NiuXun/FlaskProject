"""empty message

Revision ID: e053e75eccf4
Revises: 8dab27533dcf
Create Date: 2018-03-28 14:38:20.075623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e053e75eccf4'
down_revision = '8dab27533dcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loginlog', sa.Column('operation_type', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('loginlog', 'operation_type')
    # ### end Alembic commands ###