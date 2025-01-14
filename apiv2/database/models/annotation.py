"""
SQLAlchemy database model for Annotation

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from support.enums import annotation_method_type_enum

from platformics.database.models.base import Base
from platformics.database.models.file import File

if TYPE_CHECKING:
    from database.models.annotation_author import AnnotationAuthor
    from database.models.annotation_method_link import AnnotationMethodLink
    from database.models.annotation_shape import AnnotationShape
    from database.models.deposition import Deposition
    from database.models.run import Run

    from platformics.database.models.file import File

    ...
else:
    File = "File"
    Run = "Run"
    AnnotationShape = "AnnotationShape"
    AnnotationMethodLink = "AnnotationMethodLink"
    AnnotationAuthor = "AnnotationAuthor"
    Deposition = "Deposition"
    ...


class Annotation(Base):
    __tablename__ = "annotation"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    run_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("run.id"), nullable=True, index=True)
    run: Mapped["Run"] = relationship(
        "Run",
        foreign_keys=run_id,
        back_populates="annotations",
    )
    annotation_shapes: Mapped[list[AnnotationShape]] = relationship(
        "AnnotationShape",
        back_populates="annotation",
        uselist=True,
        foreign_keys="AnnotationShape.annotation_id",
        cascade="all, delete-orphan",
    )
    method_links: Mapped[list[AnnotationMethodLink]] = relationship(
        "AnnotationMethodLink",
        back_populates="annotation",
        uselist=True,
        foreign_keys="AnnotationMethodLink.annotation_id",
        cascade="all, delete-orphan",
    )
    authors: Mapped[list[AnnotationAuthor]] = relationship(
        "AnnotationAuthor",
        back_populates="annotation",
        uselist=True,
        foreign_keys="AnnotationAuthor.annotation_id",
        cascade="all, delete-orphan",
    )
    deposition_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("deposition.id"), nullable=True, index=True)
    deposition: Mapped["Deposition"] = relationship(
        "Deposition",
        foreign_keys=deposition_id,
        back_populates="annotations",
    )
    s3_metadata_path: Mapped[str] = mapped_column(String, nullable=False)
    https_metadata_path: Mapped[str] = mapped_column(String, nullable=False)
    annotation_publication: Mapped[str] = mapped_column(String, nullable=True)
    annotation_method: Mapped[str] = mapped_column(String, nullable=False)
    ground_truth_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    object_id: Mapped[str] = mapped_column(String, nullable=False)
    object_name: Mapped[str] = mapped_column(String, nullable=False)
    object_description: Mapped[str] = mapped_column(String, nullable=True)
    object_state: Mapped[str] = mapped_column(String, nullable=True)
    object_count: Mapped[int] = mapped_column(BigInteger, nullable=True)
    confidence_precision: Mapped[float] = mapped_column(Float, nullable=True)
    confidence_recall: Mapped[float] = mapped_column(Float, nullable=True)
    ground_truth_used: Mapped[str] = mapped_column(String, nullable=True)
    annotation_software: Mapped[str] = mapped_column(String, nullable=True)
    is_curator_recommended: Mapped[bool] = mapped_column(Boolean, nullable=True)
    method_type: Mapped[annotation_method_type_enum] = mapped_column(
        Enum(annotation_method_type_enum, native_enum=False), nullable=False,
    )
    deposition_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    release_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_modified_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, autoincrement=True, primary_key=True)
