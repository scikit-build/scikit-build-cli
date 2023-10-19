from __future__ import annotations

import importlib.metadata
import sys

__all__ = ["entry_points"]


def entry_points(*, group: str) -> importlib.metadata.EntryPoints:  # type: ignore[name-defined]
    """
    Wrapper for entry_points to support Python 3.8+ instead of 3.10+.
    """
    if sys.version_info >= (3, 10):
        return importlib.metadata.entry_points(group=group)

    epg = importlib.metadata.entry_points()

    return epg.get(group, [])


def __dir__() -> list[str]:
    return __all__
