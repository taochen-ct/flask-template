"""empty message

Revision ID: a9dad3a90e19
Revises: fb773bee63b1
Create Date: 2023-07-10 13:20:32.359228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9dad3a90e19'
down_revision = 'fb773bee63b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_bugs',
    sa.Column('uid', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('create_time', sa.Date(), nullable=False),
    sa.Column('modify_time', sa.Date(), nullable=False),
    sa.Column('module_uid', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('tb_modules',
    sa.Column('uid', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('create_time', sa.Date(), nullable=False),
    sa.Column('modify_time', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_modules')
    op.drop_table('tb_bugs')
    # ### end Alembic commands ###
