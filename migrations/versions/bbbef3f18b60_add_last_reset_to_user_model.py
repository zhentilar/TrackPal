"""Add last_reset to User model

Revision ID: bbbef3f18b60
Revises: 2c927ca8624e
Create Date: 2024-11-05 12:21:48.618962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbbef3f18b60'
down_revision = '2c927ca8624e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_reset', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_reset')

    # ### end Alembic commands ###
