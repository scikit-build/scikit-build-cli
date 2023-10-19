from __future__ import annotations

import importlib.metadata

from click.testing import CliRunner

import scikit_build_cli
import scikit_build_cli.__main__


def test_version() -> None:
    assert (
        importlib.metadata.version("scikit_build_cli") == scikit_build_cli.__version__
    )


def test_help_text() -> None:
    runner = CliRunner()
    result = runner.invoke(scikit_build_cli.__main__.skbuild, ["--help"])
    assert result.exit_code == 0
    assert "Run CMake build step" in result.output
    assert "Run CMake configure step" in result.output
