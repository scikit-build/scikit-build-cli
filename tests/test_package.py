from __future__ import annotations

import importlib.metadata

import pytest
from click.testing import CliRunner

import scikit_build_cli
import scikit_build_cli.__main__


def test_version() -> None:
    assert (
        importlib.metadata.version("scikit_build_cli") == scikit_build_cli.__version__
    )


@pytest.mark.parametrize("flag", ["--help", "-h"])
def test_help_text(flag: str) -> None:
    runner = CliRunner()
    result = runner.invoke(scikit_build_cli.__main__.skbuild, [flag])
    assert result.exit_code == 0
    assert "Run CMake build step" in result.output
    assert "Run CMake configure step" in result.output
    assert "Get the generated dynamic metadata" in result.output
    assert "Run CMake install step" in result.output
    assert "Write out the project's metadata" in result.output
    assert "Start a new project" in result.output
    assert "Add scikit-build to an existing project" in result.output
