from __future__ import annotations

import importlib.metadata as _metadata
import sys

__all__ = ["entry_points"]


def entry_points(*, group: str) -> _metadata.EntryPoints:  # type: ignore[name-defined]
    if sys.version_info >= (3, 10):
        return _metadata.entry_points(group=group)

    epg = _metadata.entry_points()

    return epg.get(group, [])


def __dir__() -> list[str]:
    return __all__
