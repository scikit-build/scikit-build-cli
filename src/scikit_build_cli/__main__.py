from __future__ import annotations

from . import skbuild


def run_cli() -> None:
    """
    Entry point to skbuild command.
    """
    skbuild()


if __name__ == "__main__":
    run_cli()
