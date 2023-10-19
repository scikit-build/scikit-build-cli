from __future__ import annotations

from typing import TYPE_CHECKING

import click

from ..utils import _build_dir

if TYPE_CHECKING:
    from pathlib import Path

__all__: list[str] = ["configure"]


def __dir__() -> list[str]:
    return __all__


@click.command()
@_build_dir
@click.help_option("--help", "-h")
@click.pass_context
def configure(ctx: click.Context, build_dir: Path) -> None:  # noqa: ARG001
    """
    Run CMake configure step
    """
    # TODO: Add specific implementations
