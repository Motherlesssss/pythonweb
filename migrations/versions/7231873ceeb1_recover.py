"""recover

Revision ID: 7231873ceeb1
Revises: 
Create Date: 2023-02-05 23:21:45.778591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7231873ceeb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Enum('BOARD', 'POST', 'COMMENT', 'FRONT_USER', 'CMS_USER', name='permissionenum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_permission_table',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], )
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('_password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('signature', sa.String(length=100), nullable=True),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role_permission_table')
    op.drop_table('role')
    op.drop_table('permission')
    # ### end Alembic commands ###
