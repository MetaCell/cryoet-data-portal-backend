"""
Factory for generating DatasetAuthor objects.

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/test_infra/factories/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long

import random
import factory
import uuid6
from database.models import DatasetAuthor
from platformics.test_infra.factories.base import FileFactory, CommonFactory
from test_infra.factories.dataset import DatasetFactory
from factory import Faker, fuzzy
from faker_biology.bioseq import Bioseq
from faker_biology.physiology import Organ
from faker_enum import EnumProvider

Faker.add_provider(Bioseq)
Faker.add_provider(Organ)
Faker.add_provider(EnumProvider)


class DatasetAuthorFactory(CommonFactory):
    class Meta:
        sqlalchemy_session = None  # workaround for a bug in factoryboy
        model = DatasetAuthor

        sqlalchemy_get_or_create = ("id",)

    dataset = factory.SubFactory(
        DatasetFactory,
        owner_user_id=factory.SelfAttribute("..owner_user_id"),
        collection_id=factory.SelfAttribute("..collection_id"),
    )
    author_list_order = fuzzy.FuzzyInteger(1, 1000)
    name = fuzzy.FuzzyText()
    email = fuzzy.FuzzyText()
    affiliation_name = fuzzy.FuzzyText()
    affiliation_address = fuzzy.FuzzyText()
    affiliation_identifier = fuzzy.FuzzyText()
    corresponding_author_status = factory.Faker("boolean")
    primary_author_status = factory.Faker("boolean")
    orcid = fuzzy.FuzzyText()
    id = fuzzy.FuzzyInteger(1, 1000)
