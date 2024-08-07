"""autogenerated

Create Date: 2024-08-07 20:20:44.483825

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20240807_162041"
down_revision = "20240807_161942"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("dataset", "cell_name", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("dataset", "cell_name", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
