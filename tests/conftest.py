"""Fixtures for lxmlh"""
import os
from pathlib import Path
from typing import List

import pytest
from lxml import etree

from lxmlh import (
    create_attribute,
    create_attribute_list,
    create_element_text,
    get_element,
    get_element_list,
    get_inner_text_list,
    parse_file,
)

DIR_DATA = os.path.join(Path(__file__).parent.parent.resolve(), "data")
FILE_SAMPLE = os.path.join(DIR_DATA, "sample.xml")
FILE_SCHEMA = os.path.join(DIR_DATA, "schema.xsd")


class ShipTo(etree.ElementBase):
    """ShipTo element."""

    name = create_element_text("name", str, FILE_SCHEMA)
    address = create_element_text("address", str, FILE_SCHEMA)
    city = create_element_text("city", str, FILE_SCHEMA)
    country = create_element_text("country", str, FILE_SCHEMA)


class Item(etree.ElementBase):
    """Item element."""

    @property
    def notes(self) -> List[str]:
        """Notes."""
        return get_inner_text_list(self, "note")


class ShipOrder(etree.ElementBase):
    """ShipOrder element."""

    orderId = create_attribute("orderid", str, FILE_SCHEMA, lambda orderId: orderId)
    orderStatus = create_attribute("orderstatus", str, FILE_SCHEMA, None)
    orderTime = create_attribute("ordertime", str, FILE_SCHEMA, None)
    orderPerson = create_element_text("orderperson", str, FILE_SCHEMA)
    discounts = create_attribute_list("discount", int, FILE_SCHEMA)

    @property
    def shipTo(self) -> "ShipTo":
        """Inner shipto element"""
        return get_element(self, "shipto")

    @property
    def itemsList(self) -> List["Item"]:
        "Items."
        return get_element_list(self, "item")


class Lookup(etree.CustomElementClassLookup):
    """Cutom lookup."""

    def lookup(self, unused_node_type, unused_document, unused_namespace, name):
        """Maps XML elements to custom classes."""
        lookupMap = {
            "item": Item,
            "shiporder": ShipOrder,
            "shipto": ShipTo,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return None


@pytest.fixture(name="ship_order")
def __ship_order() -> etree.ElementTree:
    return parse_file(FILE_SAMPLE, FILE_SCHEMA, Lookup())
