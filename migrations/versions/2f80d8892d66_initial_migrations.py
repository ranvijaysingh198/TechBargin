"""initial migrations

Revision ID: 2f80d8892d66
Revises: 
Create Date: 2021-11-03 13:16:14.326007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f80d8892d66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('register', sa.Column('f_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('register', 'f_name')
    # ### end Alembic commands ###
