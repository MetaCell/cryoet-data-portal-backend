"""autogenerated

Create Date: 2024-08-07 20:45:47.809993

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20240807_164544"
down_revision = "20240807_164408"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tomogram", "s3_prefix")
    op.drop_column("tomogram", "https_prefix")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tomogram", sa.Column("https_prefix", sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column("tomogram", sa.Column("s3_prefix", sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
