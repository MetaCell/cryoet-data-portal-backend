"""
SQLAlchemy database model for AnnotationMethodLink

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from support.enums import annotation_method_link_type_enum

from platformics.database.models.base import Base
from platformics.database.models.file import File

if TYPE_CHECKING:
    from database.models.annotation import Annotation

    from platformics.database.models.file import File

    ...
else:
    File = "File"
    Annotation = "Annotation"
    ...


class AnnotationMethodLink(Base):
    __tablename__ = "annotation_method_link"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    annotation_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("annotation.id"), nullable=True, index=True)
    annotation: Mapped["Annotation"] = relationship(
        "Annotation",
        foreign_keys=annotation_id,
        back_populates="method_links",
    )
    link_type: Mapped[annotation_method_link_type_enum] = mapped_column(
        Enum(annotation_method_link_type_enum, native_enum=False), nullable=False,
    )
    name: Mapped[str] = mapped_column(String, nullable=True)
    link: Mapped[str] = mapped_column(String, nullable=False)
    id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, autoincrement=True, primary_key=True)
