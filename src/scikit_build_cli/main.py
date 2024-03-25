from __future__ import annotations

import pathlib
from collections.abc import MutableMapping, Sequence
from importlib.metadata import EntryPoint

import click

from . import __version__
from ._compat.importlib import metadata

__all__ = ["skbuild"]


def __dir__() -> list[str]:
    return __all__


class LazyGroup(click.Group):
    """
    Lazy loader for click commands. Based on Click's documentation, but uses
    EntryPoints.
    """

    def __init__(
        self,
        name: str | None = None,
        commands: (
            MutableMapping[str, click.Command] | Sequence[click.Command] | None
        ) = None,
        *,
        lazy_subcommands: Sequence[EntryPoint] = (),
        **kwargs: object,
    ):
        super().__init__(name, commands, **kwargs)
        self.lazy_subcommands = {v.name: v for v in lazy_subcommands}

    def list_commands(self, ctx: click.Context) -> list[str]:
        return sorted([*super().list_commands(ctx), *self.lazy_subcommands])

    def get_command(self, ctx: click.Context, cmd_name: str) -> click.Command | None:
        if cmd_name in self.lazy_subcommands:
            return self._lazy_load(cmd_name)
        return super().get_command(ctx, cmd_name)

    def _lazy_load(self, cmd_name: str) -> click.Command:
        ep = self.lazy_subcommands[cmd_name]
        cmd_object = ep.load()
        if not isinstance(cmd_object, click.Command):
            msg = f"Lazy loading of {ep} failed by returning a non-command object"
            raise ValueError(msg)
        return cmd_object


# Add all plugin commands.
CMDS = list(metadata.entry_points(group="skbuild.commands"))


@click.group("skbuild", cls=LazyGroup, lazy_subcommands=CMDS)
@click.version_option(__version__)
@click.option(
    "--root",
    "-r",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        path_type=pathlib.Path,
    ),
    help="Path to the Python project's root",
)
@click.pass_context
def skbuild(ctx: click.Context, root: pathlib.Path) -> None:  # noqa: ARG001
    """
    scikit-build Main CLI interface
    """
    # TODO: Add specific implementations
