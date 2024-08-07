"""autogenerated

Create Date: 2024-08-07 20:30:12.429538

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "20240807_163009"
down_revision = "20240807_162823"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tomogram",
        sa.Column(
            "tomogram_type",
            sa.Enum("CANONICAL", "UNKNOWN", name="tomogram_type_enum", native_enum=False),
            nullable=True,
        ),
    )
    op.drop_column("tomogram", "type")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tomogram", sa.Column("type", sa.VARCHAR(length=9), autoincrement=False, nullable=True))
    op.drop_column("tomogram", "tomogram_type")
    # ### end Alembic commands ###
