"""
SQLAlchemy database model for TomogramAuthor

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from platformics.database.models.base import Base
from platformics.database.models.file import File

if TYPE_CHECKING:
    from database.models.tomogram import Tomogram

    from platformics.database.models.file import File

    ...
else:
    File = "File"
    Tomogram = "Tomogram"
    ...


class TomogramAuthor(Base):
    __tablename__ = "tomogram_author"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    tomogram_id: Mapped[int] = mapped_column(Integer, ForeignKey("tomogram.id"), nullable=True, index=True)
    tomogram: Mapped["Tomogram"] = relationship(
        "Tomogram",
        foreign_keys=tomogram_id,
        back_populates="authors",
    )
    id: Mapped[int] = mapped_column(Integer, nullable=False, index=True, autoincrement=True, primary_key=True)
    author_list_order: Mapped[int] = mapped_column(Integer, nullable=False)
    orcid: Mapped[str] = mapped_column(String, nullable=True)
    kaggle_id: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_name: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_address: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_identifier: Mapped[str] = mapped_column(String, nullable=True)
    corresponding_author_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    primary_author_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
