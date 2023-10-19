from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import click

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, TypeVar

    F = TypeVar("F", bound=Callable[..., Any])


__all__: list[str] = ["_build_dir"]


def __dir__() -> list[str]:
    return __all__


_build_dir = click.option(
    "--build-dir",
    "-B",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        path_type=pathlib.Path,
    ),
    help="Path to cmake build directory",
)
