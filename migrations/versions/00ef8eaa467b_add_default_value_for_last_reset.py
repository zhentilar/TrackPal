"""Add default value for last_reset

Revision ID: 00ef8eaa467b
Revises: bbbef3f18b60
Create Date: 2024-11-05 12:23:49.340543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00ef8eaa467b'
down_revision = 'bbbef3f18b60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATE(), nullable=True))

    # ### end Alembic commands ###
