from __future__ import annotations

import click

__all__: list[str] = ["init"]


def __dir__() -> list[str]:
    return __all__


@click.command()
@click.help_option("--help", "-h")
@click.pass_context
def init(ctx: click.Context) -> None:  # noqa: ARG001
    """
    Add scikit-build to an existing project
    """
    # TODO: Add specific implementations
