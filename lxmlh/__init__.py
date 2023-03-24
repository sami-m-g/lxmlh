"""lxmlh."""
import importlib.metadata
from typing import Union

from .config import TIMESTAMP_FORMAT, TYPE_DEFAULTS, TYPE_FUNC_MAP
from .helpers import (
    create_attribute,
    create_element_text,
    fill_in_defaults,
    get_attribute,
    get_attribute_list,
    get_element,
    get_element_list,
    get_element_text,
    get_inner_text_list,
    set_attribute,
    set_attribute_list,
    set_element_text,
)

__all__ = (
    "__version__",
    "fill_in_defaults",
    "create_attribute",
    "create_element_text",
    "get_attribute",
    "get_element",
    "get_attribute_list",
    "get_element_text",
    "get_element_list",
    "get_inner_text_list",
    "set_attribute",
    "set_attribute_list",
    "set_element_text",
    "TIMESTAMP_FORMAT",
    "TYPE_DEFAULTS",
    "TYPE_FUNC_MAP",
)


def _get_version_tuple() -> tuple:
    def as_integer(string: str) -> Union[int, str]:
        try:
            return int(string)
        except ValueError:
            return string

    return tuple(
        as_integer(v) for v in importlib.metadata.version("lxmlh").strip().split(".")
    )


__version__ = _get_version_tuple()
