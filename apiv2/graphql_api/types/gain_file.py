"""
GraphQL type for GainFile

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/graphql_api/types/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long


import datetime
import enum
import typing
from typing import TYPE_CHECKING, Annotated, Optional, Sequence

import database.models as db
import strawberry
from fastapi import Depends
from graphql_api.helpers.gain_file import GainFileGroupByOptions, build_gain_file_groupby_output
from sqlalchemy import inspect
from sqlalchemy.engine.row import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.types import Info
from support.limit_offset import LimitOffsetClause
from typing_extensions import TypedDict
from validators.gain_file import GainFileCreateInputValidator, GainFileUpdateInputValidator

from platformics.graphql_api.core.deps import get_authz_client, get_db_session, is_system_user, require_auth_principal
from platformics.graphql_api.core.errors import PlatformicsError
from platformics.graphql_api.core.query_builder import get_aggregate_db_rows, get_db_rows
from platformics.graphql_api.core.query_input_types import (
    IntComparators,
    StrComparators,
    aggregator_map,
    orderBy,
)
from platformics.graphql_api.core.relay_interface import EntityInterface
from platformics.graphql_api.core.strawberry_extensions import DependencyExtension
from platformics.security.authorization import AuthzAction, AuthzClient, Principal

E = typing.TypeVar("E")
T = typing.TypeVar("T")

if TYPE_CHECKING:
    from graphql_api.types.run import Run, RunOrderByClause, RunWhereClause

    pass
else:
    RunWhereClause = "RunWhereClause"
    Run = "Run"
    RunOrderByClause = "RunOrderByClause"
    pass


"""
------------------------------------------------------------------------------
Dataloaders
------------------------------------------------------------------------------
These are batching functions for loading related objects to avoid N+1 queries.
"""


@strawberry.field
async def load_run_rows(
    root: "GainFile",
    info: Info,
    where: Annotated["RunWhereClause", strawberry.lazy("graphql_api.types.run")] | None = None,
    order_by: Optional[list[Annotated["RunOrderByClause", strawberry.lazy("graphql_api.types.run")]]] = [],
) -> Optional[Annotated["Run", strawberry.lazy("graphql_api.types.run")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.GainFile)
    relationship = mapper.relationships["run"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.run_id)  # type:ignore


"""
------------------------------------------------------------------------------
Define Strawberry GQL types
------------------------------------------------------------------------------
"""


"""
Only let users specify IDs in WHERE clause when mutating data (for safety).
We can extend that list as we gather more use cases from the FE team.
"""


@strawberry.input
class GainFileWhereClauseMutations(TypedDict):
    id: IntComparators | None


"""
Supported WHERE clause attributes
"""


@strawberry.input
class GainFileWhereClause(TypedDict):
    run: Optional[Annotated["RunWhereClause", strawberry.lazy("graphql_api.types.run")]] | None
    run_id: Optional[IntComparators] | None
    s3_file_path: Optional[StrComparators] | None
    https_file_path: Optional[StrComparators] | None
    id: Optional[IntComparators] | None


"""
Supported ORDER BY clause attributes
"""


@strawberry.input
class GainFileOrderByClause(TypedDict):
    run: Optional[Annotated["RunOrderByClause", strawberry.lazy("graphql_api.types.run")]] | None
    s3_file_path: Optional[orderBy] | None
    https_file_path: Optional[orderBy] | None
    id: Optional[orderBy] | None


"""
Define GainFile type
"""


@strawberry.type(description="Gain values for frames in this run")
class GainFile(EntityInterface):
    run: Optional[Annotated["Run", strawberry.lazy("graphql_api.types.run")]] = load_run_rows  # type:ignore
    run_id: Optional[int]
    s3_file_path: str = strawberry.field(description="Path to the file in s3")
    https_file_path: str = strawberry.field(description="Path to the file as an https url")
    id: int = strawberry.field(description="Numeric identifier (May change!)")


"""
We need to add this to each Queryable type so that strawberry will accept either our
Strawberry type *or* a SQLAlchemy model instance as a valid response class from a resolver
"""
GainFile.__strawberry_definition__.is_type_of = (  # type: ignore
    lambda obj, info: type(obj) == db.GainFile or type(obj) == GainFile
)

"""
------------------------------------------------------------------------------
Aggregation types
------------------------------------------------------------------------------
"""
"""
Define columns that support numerical aggregations
"""


@strawberry.type
class GainFileNumericalColumns:
    id: Optional[int] = None


"""
Define columns that support min/max aggregations
"""


@strawberry.type
class GainFileMinMaxColumns:
    s3_file_path: Optional[str] = None
    https_file_path: Optional[str] = None
    id: Optional[int] = None


"""
Define enum of all columns to support count and count(distinct) aggregations
"""


@strawberry.enum
class GainFileCountColumns(enum.Enum):
    run = "run"
    s3FilePath = "s3_file_path"
    httpsFilePath = "https_file_path"
    id = "id"


"""
All supported aggregation functions
"""


@strawberry.type
class GainFileAggregateFunctions:
    # This is a hack to accept "distinct" and "columns" as arguments to "count"
    @strawberry.field
    def count(self, distinct: Optional[bool] = False, columns: Optional[GainFileCountColumns] = None) -> Optional[int]:
        # Count gets set with the proper value in the resolver, so we just return it here
        return self.count  # type: ignore

    sum: Optional[GainFileNumericalColumns] = None
    avg: Optional[GainFileNumericalColumns] = None
    stddev: Optional[GainFileNumericalColumns] = None
    variance: Optional[GainFileNumericalColumns] = None
    min: Optional[GainFileMinMaxColumns] = None
    max: Optional[GainFileMinMaxColumns] = None
    groupBy: Optional[GainFileGroupByOptions] = None


"""
Wrapper around GainFileAggregateFunctions
"""


@strawberry.type
class GainFileAggregate:
    aggregate: Optional[list[GainFileAggregateFunctions]] = None


"""
------------------------------------------------------------------------------
Mutation types
------------------------------------------------------------------------------
"""


@strawberry.input()
class GainFileCreateInput:
    run_id: Optional[strawberry.ID] = strawberry.field(description=None, default=None)
    s3_file_path: str = strawberry.field(description="Path to the file in s3")
    https_file_path: str = strawberry.field(description="Path to the file as an https url")
    id: int = strawberry.field(description="Numeric identifier (May change!)")


@strawberry.input()
class GainFileUpdateInput:
    run_id: Optional[strawberry.ID] = strawberry.field(description=None, default=None)
    s3_file_path: Optional[str] = strawberry.field(description="Path to the file in s3")
    https_file_path: Optional[str] = strawberry.field(description="Path to the file as an https url")
    id: Optional[int] = strawberry.field(description="Numeric identifier (May change!)")


"""
------------------------------------------------------------------------------
Utilities
------------------------------------------------------------------------------
"""


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_gain_files(
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[GainFileWhereClause] = None,
    order_by: Optional[list[GainFileOrderByClause]] = [],
    limit_offset: Optional[LimitOffsetClause] = None,
) -> typing.Sequence[GainFile]:
    """
    Resolve GainFile objects. Used for queries (see graphql_api/queries.py).
    """
    limit = limit_offset["limit"] if limit_offset and "limit" in limit_offset else None
    offset = limit_offset["offset"] if limit_offset and "offset" in limit_offset else None
    if offset and not limit:
        raise PlatformicsError("Cannot use offset without limit")
    return await get_db_rows(db.GainFile, session, authz_client, principal, where, order_by, AuthzAction.VIEW, limit, offset)  # type: ignore


def format_gain_file_aggregate_output(query_results: Sequence[RowMapping] | RowMapping) -> GainFileAggregate:
    """
    Given a row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    aggregate = []
    if type(query_results) is not list:
        query_results = [query_results]  # type: ignore
    for row in query_results:
        aggregate.append(format_gain_file_aggregate_row(row))
    return GainFileAggregate(aggregate=aggregate)


def format_gain_file_aggregate_row(row: RowMapping) -> GainFileAggregateFunctions:
    """
    Given a single row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    output = GainFileAggregateFunctions()
    for key, value in row.items():
        # Key is either an aggregate function or a groupby key
        group_keys = key.split(".")
        aggregate = key.split("_", 1)
        if aggregate[0] not in aggregator_map.keys():
            # Turn list of groupby keys into nested objects
            if not output.groupBy:
                output.groupBy = GainFileGroupByOptions()
            group = build_gain_file_groupby_output(output.groupBy, group_keys, value)
            output.groupBy = group
        else:
            aggregate_name = aggregate[0]
            if aggregate_name == "count":
                output.count = value
            else:
                aggregator_fn, col_name = aggregate[0], aggregate[1]
                if not getattr(output, aggregator_fn):
                    if aggregate_name in ["min", "max"]:
                        setattr(output, aggregator_fn, GainFileMinMaxColumns())
                    else:
                        setattr(output, aggregator_fn, GainFileNumericalColumns())
                setattr(getattr(output, aggregator_fn), col_name, value)
    return output


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_gain_files_aggregate(
    info: Info,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[GainFileWhereClause] = None,
    # TODO: add support for groupby, limit/offset
) -> GainFileAggregate:
    """
    Aggregate values for GainFile objects. Used for queries (see graphql_api/queries.py).
    """
    # Get the selected aggregate functions and columns to operate on, and groupby options if any were provided.
    # TODO: not sure why selected_fields is a list
    selections = info.selected_fields[0].selections[0].selections
    aggregate_selections = [selection for selection in selections if selection.name != "groupBy"]
    groupby_selections = [selection for selection in selections if selection.name == "groupBy"]
    groupby_selections = groupby_selections[0].selections if groupby_selections else []

    if not aggregate_selections:
        raise PlatformicsError("No aggregate functions selected")

    rows = await get_aggregate_db_rows(db.GainFile, session, authz_client, principal, where, aggregate_selections, [], groupby_selections)  # type: ignore
    aggregate_output = format_gain_file_aggregate_output(rows)
    return aggregate_output


@strawberry.mutation(extensions=[DependencyExtension()])
async def create_gain_file(
    input: GainFileCreateInput,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> db.GainFile:
    """
    Create a new GainFile object. Used for mutations (see graphql_api/mutations.py).
    """
    validated = GainFileCreateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Validate that the user can read all of the entities they're linking to.

    # Validate that the user can read all of the entities they're linking to.
    # Check that run relationship is accessible.
    if validated.run_id:
        run = await get_db_rows(
            db.Run, session, authz_client, principal, {"id": {"_eq": validated.run_id}}, [], AuthzAction.VIEW,
        )
        if not run:
            raise PlatformicsError("Unauthorized: run does not exist")

    # Save to DB
    params["owner_user_id"] = int(principal.id)
    new_entity = db.GainFile(**params)

    # Are we actually allowed to create this entity?
    if not authz_client.can_create(new_entity, principal):
        raise PlatformicsError("Unauthorized: Cannot create entity")

    session.add(new_entity)
    await session.commit()
    return new_entity


@strawberry.mutation(extensions=[DependencyExtension()])
async def update_gain_file(
    input: GainFileUpdateInput,
    where: GainFileWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> Sequence[db.GainFile]:
    """
    Update GainFile objects. Used for mutations (see graphql_api/mutations.py).
    """
    validated = GainFileUpdateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Need at least one thing to update
    num_params = len([x for x in params if params[x] is not None])
    if num_params == 0:
        raise PlatformicsError("No fields to update")

    # Validate that the user can read all of the entities they're linking to.
    # Check that run relationship is accessible.
    if validated.run_id:
        run = await get_db_rows(
            db.Run, session, authz_client, principal, {"id": {"_eq": validated.run_id}}, [], AuthzAction.VIEW,
        )
        if not run:
            raise PlatformicsError("Unauthorized: run does not exist")
        params["run"] = run[0]
        del params["run_id"]

    # Fetch entities for update, if we have access to them
    entities = await get_db_rows(db.GainFile, session, authz_client, principal, where, [], AuthzAction.UPDATE)
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot update entities")

    # Update DB
    updated_at = datetime.datetime.now()
    for entity in entities:
        entity.updated_at = updated_at
        for key in params:
            if params[key] is not None:
                setattr(entity, key, params[key])

    if not authz_client.can_update(entity, principal):
        raise PlatformicsError("Unauthorized: Cannot access new collection")

    await session.commit()
    return entities


@strawberry.mutation(extensions=[DependencyExtension()])
async def delete_gain_file(
    where: GainFileWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
) -> Sequence[db.GainFile]:
    """
    Delete GainFile objects. Used for mutations (see graphql_api/mutations.py).
    """
    # Fetch entities for deletion, if we have access to them
    entities = await get_db_rows(db.GainFile, session, authz_client, principal, where, [], AuthzAction.DELETE)
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot delete entities")

    # Update DB
    for entity in entities:
        await session.delete(entity)
    await session.commit()
    return entities
