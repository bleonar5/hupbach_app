"""empty message

Revision ID: 07fa9957f9d6
Revises: 
Create Date: 2021-05-16 09:14:31.515693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07fa9957f9d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.String(length=64), nullable=True),
    sa.Column('object_type', sa.String(length=64), nullable=True),
    sa.Column('version', sa.String(length=64), nullable=True),
    sa.Column('reactivation', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_pid'), 'users', ['pid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_pid'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###