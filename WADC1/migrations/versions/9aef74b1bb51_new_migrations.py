"""new migrations

Revision ID: 9aef74b1bb51
Revises: 
Create Date: 2023-10-20 17:40:24.527098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aef74b1bb51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expense', sa.Float(), nullable=True),
    sa.Column('expensetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Float(), nullable=True),
    sa.Column('incometime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('income')
    op.drop_table('expense')
    # ### end Alembic commands ###
