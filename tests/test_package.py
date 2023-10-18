from __future__ import annotations

import importlib.metadata

import scikit_build_cli as m


def test_version():
    assert importlib.metadata.version("scikit_build_cli") == m.__version__
