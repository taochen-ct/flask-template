"""empty message

Revision ID: 3889551926b3
Revises: a9dad3a90e19
Create Date: 2023-07-10 15:19:02.286856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3889551926b3'
down_revision = 'a9dad3a90e19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_bugs', schema=None) as batch_op:
        batch_op.alter_column('create_time',
               existing_type=sa.DATE(),
               type_=sa.String(length=30),
               existing_nullable=False)
        batch_op.alter_column('modify_time',
               existing_type=sa.DATE(),
               type_=sa.String(length=30),
               existing_nullable=False)

    with op.batch_alter_table('tb_modules', schema=None) as batch_op:
        batch_op.alter_column('create_time',
               existing_type=sa.DATE(),
               type_=sa.String(length=30),
               existing_nullable=False)
        batch_op.alter_column('modify_time',
               existing_type=sa.DATE(),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_modules', schema=None) as batch_op:
        batch_op.alter_column('modify_time',
               existing_type=sa.String(length=30),
               type_=sa.DATE(),
               existing_nullable=False)
        batch_op.alter_column('create_time',
               existing_type=sa.String(length=30),
               type_=sa.DATE(),
               existing_nullable=False)

    with op.batch_alter_table('tb_bugs', schema=None) as batch_op:
        batch_op.alter_column('modify_time',
               existing_type=sa.String(length=30),
               type_=sa.DATE(),
               existing_nullable=False)
        batch_op.alter_column('create_time',
               existing_type=sa.String(length=30),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
