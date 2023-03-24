"""lxmlh."""
import importlib.metadata
from typing import Union


def _get_version_tuple() -> tuple:
    def as_integer(string: str) -> Union[int, str]:
        try:
            return int(string)
        except ValueError:
            return string

    return tuple(
        as_integer(v)
        for v in importlib.metadata.version("lxmlh")
        .strip()
        .split(".")
    )

__version__ = _get_version_tuple()