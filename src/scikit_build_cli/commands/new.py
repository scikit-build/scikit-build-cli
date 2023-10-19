from __future__ import annotations

import click

__all__: list[str] = ["new"]


def __dir__() -> list[str]:
    return __all__


@click.command()
@click.help_option("--help", "-h")
@click.pass_context
def new(ctx: click.Context) -> None:  # noqa: ARG001
    """
    Start a new project
    """
    # TODO: Add specific implementations
