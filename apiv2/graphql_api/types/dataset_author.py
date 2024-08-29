"""
GraphQL type for DatasetAuthor

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
from graphql_api.helpers.dataset_author import DatasetAuthorGroupByOptions, build_dataset_author_groupby_output
from sqlalchemy import inspect
from sqlalchemy.engine.row import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.types import Info
from support.limit_offset import LimitOffsetClause
from typing_extensions import TypedDict
from validators.dataset_author import DatasetAuthorCreateInputValidator, DatasetAuthorUpdateInputValidator

from platformics.graphql_api.core.deps import get_authz_client, get_db_session, is_system_user, require_auth_principal
from platformics.graphql_api.core.errors import PlatformicsError
from platformics.graphql_api.core.query_builder import get_aggregate_db_rows, get_db_rows
from platformics.graphql_api.core.query_input_types import (
    BoolComparators,
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
    from graphql_api.types.dataset import Dataset, DatasetOrderByClause, DatasetWhereClause

    pass
else:
    DatasetWhereClause = "DatasetWhereClause"
    Dataset = "Dataset"
    DatasetOrderByClause = "DatasetOrderByClause"
    pass


"""
------------------------------------------------------------------------------
Dataloaders
------------------------------------------------------------------------------
These are batching functions for loading related objects to avoid N+1 queries.
"""


@strawberry.field
async def load_dataset_rows(
    root: "DatasetAuthor",
    info: Info,
    where: Annotated["DatasetWhereClause", strawberry.lazy("graphql_api.types.dataset")] | None = None,
    order_by: Optional[list[Annotated["DatasetOrderByClause", strawberry.lazy("graphql_api.types.dataset")]]] = [],
) -> Optional[Annotated["Dataset", strawberry.lazy("graphql_api.types.dataset")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.DatasetAuthor)
    relationship = mapper.relationships["dataset"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.dataset_id)  # type:ignore


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
class DatasetAuthorWhereClauseMutations(TypedDict):
    id: IntComparators | None


"""
Supported WHERE clause attributes
"""


@strawberry.input
class DatasetAuthorWhereClause(TypedDict):
    dataset: Optional[Annotated["DatasetWhereClause", strawberry.lazy("graphql_api.types.dataset")]] | None
    id: Optional[IntComparators] | None
    author_list_order: Optional[IntComparators] | None
    orcid: Optional[StrComparators] | None
    name: Optional[StrComparators] | None
    email: Optional[StrComparators] | None
    affiliation_name: Optional[StrComparators] | None
    affiliation_address: Optional[StrComparators] | None
    affiliation_identifier: Optional[StrComparators] | None
    corresponding_author_status: Optional[BoolComparators] | None
    primary_author_status: Optional[BoolComparators] | None


"""
Supported ORDER BY clause attributes
"""


@strawberry.input
class DatasetAuthorOrderByClause(TypedDict):
    dataset: Optional[Annotated["DatasetOrderByClause", strawberry.lazy("graphql_api.types.dataset")]] | None
    id: Optional[orderBy] | None
    author_list_order: Optional[orderBy] | None
    orcid: Optional[orderBy] | None
    name: Optional[orderBy] | None
    email: Optional[orderBy] | None
    affiliation_name: Optional[orderBy] | None
    affiliation_address: Optional[orderBy] | None
    affiliation_identifier: Optional[orderBy] | None
    corresponding_author_status: Optional[orderBy] | None
    primary_author_status: Optional[orderBy] | None


"""
Define DatasetAuthor type
"""


@strawberry.type(description="An author of a dataset")
class DatasetAuthor(EntityInterface):
    dataset: Optional[Annotated["Dataset", strawberry.lazy("graphql_api.types.dataset")]] = (
        load_dataset_rows
    )  # type:ignore
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")
    author_list_order: int = strawberry.field(
        description="The order that the author is listed as in the associated publication",
    )
    orcid: Optional[str] = strawberry.field(description="The ORCID identifier for the author.", default=None)
    name: str = strawberry.field(description="The full name of the author.")
    email: Optional[str] = strawberry.field(description="The email address of the author.", default=None)
    affiliation_name: Optional[str] = strawberry.field(
        description="The name of the author's affiliation.", default=None,
    )
    affiliation_address: Optional[str] = strawberry.field(
        description="The address of the author's affiliation.", default=None,
    )
    affiliation_identifier: Optional[str] = strawberry.field(
        description="A Research Organization Registry (ROR) identifier.", default=None,
    )
    corresponding_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a corresponding author.", default=None,
    )
    primary_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a primary author.", default=None,
    )


"""
We need to add this to each Queryable type so that strawberry will accept either our
Strawberry type *or* a SQLAlchemy model instance as a valid response class from a resolver
"""
DatasetAuthor.__strawberry_definition__.is_type_of = (  # type: ignore
    lambda obj, info: type(obj) == db.DatasetAuthor or type(obj) == DatasetAuthor
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
class DatasetAuthorNumericalColumns:
    id: Optional[int] = None
    author_list_order: Optional[int] = None


"""
Define columns that support min/max aggregations
"""


@strawberry.type
class DatasetAuthorMinMaxColumns:
    id: Optional[int] = None
    author_list_order: Optional[int] = None
    orcid: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    affiliation_name: Optional[str] = None
    affiliation_address: Optional[str] = None
    affiliation_identifier: Optional[str] = None


"""
Define enum of all columns to support count and count(distinct) aggregations
"""


@strawberry.enum
class DatasetAuthorCountColumns(enum.Enum):
    dataset = "dataset"
    id = "id"
    authorListOrder = "author_list_order"
    orcid = "orcid"
    name = "name"
    email = "email"
    affiliationName = "affiliation_name"
    affiliationAddress = "affiliation_address"
    affiliationIdentifier = "affiliation_identifier"
    correspondingAuthorStatus = "corresponding_author_status"
    primaryAuthorStatus = "primary_author_status"


"""
All supported aggregation functions
"""


@strawberry.type
class DatasetAuthorAggregateFunctions:
    # This is a hack to accept "distinct" and "columns" as arguments to "count"
    @strawberry.field
    def count(
        self, distinct: Optional[bool] = False, columns: Optional[DatasetAuthorCountColumns] = None,
    ) -> Optional[int]:
        # Count gets set with the proper value in the resolver, so we just return it here
        return self.count  # type: ignore

    sum: Optional[DatasetAuthorNumericalColumns] = None
    avg: Optional[DatasetAuthorNumericalColumns] = None
    stddev: Optional[DatasetAuthorNumericalColumns] = None
    variance: Optional[DatasetAuthorNumericalColumns] = None
    min: Optional[DatasetAuthorMinMaxColumns] = None
    max: Optional[DatasetAuthorMinMaxColumns] = None
    groupBy: Optional[DatasetAuthorGroupByOptions] = None


"""
Wrapper around DatasetAuthorAggregateFunctions
"""


@strawberry.type
class DatasetAuthorAggregate:
    aggregate: Optional[list[DatasetAuthorAggregateFunctions]] = None


"""
------------------------------------------------------------------------------
Mutation types
------------------------------------------------------------------------------
"""


@strawberry.input()
class DatasetAuthorCreateInput:
    dataset_id: Optional[strawberry.ID] = strawberry.field(description="An author of a dataset", default=None)
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")
    author_list_order: int = strawberry.field(
        description="The order that the author is listed as in the associated publication",
    )
    orcid: Optional[str] = strawberry.field(description="The ORCID identifier for the author.", default=None)
    name: str = strawberry.field(description="The full name of the author.")
    email: Optional[str] = strawberry.field(description="The email address of the author.", default=None)
    affiliation_name: Optional[str] = strawberry.field(
        description="The name of the author's affiliation.", default=None,
    )
    affiliation_address: Optional[str] = strawberry.field(
        description="The address of the author's affiliation.", default=None,
    )
    affiliation_identifier: Optional[str] = strawberry.field(
        description="A Research Organization Registry (ROR) identifier.", default=None,
    )
    corresponding_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a corresponding author.", default=None,
    )
    primary_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a primary author.", default=None,
    )


@strawberry.input()
class DatasetAuthorUpdateInput:
    dataset_id: Optional[strawberry.ID] = strawberry.field(description="An author of a dataset", default=None)
    id: Optional[int] = strawberry.field(description="An identifier to refer to a specific instance of this type")
    author_list_order: Optional[int] = strawberry.field(
        description="The order that the author is listed as in the associated publication",
    )
    orcid: Optional[str] = strawberry.field(description="The ORCID identifier for the author.", default=None)
    name: Optional[str] = strawberry.field(description="The full name of the author.")
    email: Optional[str] = strawberry.field(description="The email address of the author.", default=None)
    affiliation_name: Optional[str] = strawberry.field(
        description="The name of the author's affiliation.", default=None,
    )
    affiliation_address: Optional[str] = strawberry.field(
        description="The address of the author's affiliation.", default=None,
    )
    affiliation_identifier: Optional[str] = strawberry.field(
        description="A Research Organization Registry (ROR) identifier.", default=None,
    )
    corresponding_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a corresponding author.", default=None,
    )
    primary_author_status: Optional[bool] = strawberry.field(
        description="Whether the author is a primary author.", default=None,
    )


"""
------------------------------------------------------------------------------
Utilities
------------------------------------------------------------------------------
"""


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_dataset_authors(
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[DatasetAuthorWhereClause] = None,
    order_by: Optional[list[DatasetAuthorOrderByClause]] = [],
    limit_offset: Optional[LimitOffsetClause] = None,
) -> typing.Sequence[DatasetAuthor]:
    """
    Resolve DatasetAuthor objects. Used for queries (see graphql_api/queries.py).
    """
    limit = limit_offset["limit"] if limit_offset and "limit" in limit_offset else None
    offset = limit_offset["offset"] if limit_offset and "offset" in limit_offset else None
    if offset and not limit:
        raise PlatformicsError("Cannot use offset without limit")
    return await get_db_rows(db.DatasetAuthor, session, authz_client, principal, where, order_by, AuthzAction.VIEW, limit, offset)  # type: ignore


def format_dataset_author_aggregate_output(query_results: Sequence[RowMapping] | RowMapping) -> DatasetAuthorAggregate:
    """
    Given a row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    aggregate = []
    if type(query_results) is not list:
        query_results = [query_results]  # type: ignore
    for row in query_results:
        aggregate.append(format_dataset_author_aggregate_row(row))
    return DatasetAuthorAggregate(aggregate=aggregate)


def format_dataset_author_aggregate_row(row: RowMapping) -> DatasetAuthorAggregateFunctions:
    """
    Given a single row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    output = DatasetAuthorAggregateFunctions()
    for key, value in row.items():
        # Key is either an aggregate function or a groupby key
        group_keys = key.split(".")
        aggregate = key.split("_", 1)
        if aggregate[0] not in aggregator_map.keys():
            # Turn list of groupby keys into nested objects
            if not output.groupBy:
                output.groupBy = DatasetAuthorGroupByOptions()
            group = build_dataset_author_groupby_output(output.groupBy, group_keys, value)
            output.groupBy = group
        else:
            aggregate_name = aggregate[0]
            if aggregate_name == "count":
                output.count = value
            else:
                aggregator_fn, col_name = aggregate[0], aggregate[1]
                if not getattr(output, aggregator_fn):
                    if aggregate_name in ["min", "max"]:
                        setattr(output, aggregator_fn, DatasetAuthorMinMaxColumns())
                    else:
                        setattr(output, aggregator_fn, DatasetAuthorNumericalColumns())
                setattr(getattr(output, aggregator_fn), col_name, value)
    return output


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_dataset_authors_aggregate(
    info: Info,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[DatasetAuthorWhereClause] = None,
    # TODO: add support for groupby, limit/offset
) -> DatasetAuthorAggregate:
    """
    Aggregate values for DatasetAuthor objects. Used for queries (see graphql_api/queries.py).
    """
    # Get the selected aggregate functions and columns to operate on, and groupby options if any were provided.
    # TODO: not sure why selected_fields is a list
    selections = info.selected_fields[0].selections[0].selections
    aggregate_selections = [selection for selection in selections if selection.name != "groupBy"]
    groupby_selections = [selection for selection in selections if selection.name == "groupBy"]
    groupby_selections = groupby_selections[0].selections if groupby_selections else []

    if not aggregate_selections:
        raise PlatformicsError("No aggregate functions selected")

    rows = await get_aggregate_db_rows(db.DatasetAuthor, session, authz_client, principal, where, aggregate_selections, [], groupby_selections)  # type: ignore
    aggregate_output = format_dataset_author_aggregate_output(rows)
    return aggregate_output


@strawberry.mutation(extensions=[DependencyExtension()])
async def create_dataset_author(
    input: DatasetAuthorCreateInput,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> db.DatasetAuthor:
    """
    Create a new DatasetAuthor object. Used for mutations (see graphql_api/mutations.py).
    """
    validated = DatasetAuthorCreateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Validate that the user can read all of the entities they're linking to.

    # Validate that the user can read all of the entities they're linking to.
    # Check that dataset relationship is accessible.
    if validated.dataset_id:
        dataset = await get_db_rows(
            db.Dataset, session, authz_client, principal, {"id": {"_eq": validated.dataset_id}}, [], AuthzAction.VIEW,
        )
        if not dataset:
            raise PlatformicsError("Unauthorized: dataset does not exist")

    # Save to DB
    params["owner_user_id"] = int(principal.id)
    new_entity = db.DatasetAuthor(**params)

    # Are we actually allowed to create this entity?
    if not authz_client.can_create(new_entity, principal):
        raise PlatformicsError("Unauthorized: Cannot create entity")

    session.add(new_entity)
    await session.commit()
    return new_entity


@strawberry.mutation(extensions=[DependencyExtension()])
async def update_dataset_author(
    input: DatasetAuthorUpdateInput,
    where: DatasetAuthorWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> Sequence[db.DatasetAuthor]:
    """
    Update DatasetAuthor objects. Used for mutations (see graphql_api/mutations.py).
    """
    validated = DatasetAuthorUpdateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Need at least one thing to update
    num_params = len([x for x in params if params[x] is not None])
    if num_params == 0:
        raise PlatformicsError("No fields to update")

    # Validate that the user can read all of the entities they're linking to.
    # Check that dataset relationship is accessible.
    if validated.dataset_id:
        dataset = await get_db_rows(
            db.Dataset, session, authz_client, principal, {"id": {"_eq": validated.dataset_id}}, [], AuthzAction.VIEW,
        )
        if not dataset:
            raise PlatformicsError("Unauthorized: dataset does not exist")
        params["dataset"] = dataset[0]
        del params["dataset_id"]

    # Fetch entities for update, if we have access to them
    entities = await get_db_rows(db.DatasetAuthor, session, authz_client, principal, where, [], AuthzAction.UPDATE)
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
async def delete_dataset_author(
    where: DatasetAuthorWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
) -> Sequence[db.DatasetAuthor]:
    """
    Delete DatasetAuthor objects. Used for mutations (see graphql_api/mutations.py).
    """
    # Fetch entities for deletion, if we have access to them
    entities = await get_db_rows(db.DatasetAuthor, session, authz_client, principal, where, [], AuthzAction.DELETE)
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot delete entities")

    # Update DB
    for entity in entities:
        await session.delete(entity)
    await session.commit()
    return entities
