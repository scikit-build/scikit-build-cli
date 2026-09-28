from __future__ import annotations

from ._version import version as __version__

# Load all subcommands
# Load and expose the main CLI interface
from .main import skbuild

__all__: list[str] = ["__version__", "skbuild"]
