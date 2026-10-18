"""Run the actual runtime syntax contract; do not execute UI code in Node."""
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")
pytestmark = pytest.mark.skipif(NODE is None, reason="Node is required for runtime syntax checks")


def run_smoke(script, cwd):
    return subprocess.run([NODE, str(script)], cwd=cwd, capture_output=True,
                          text=True, timeout=30)


def test_runtime_files_pass_from_another_working_directory(tmp_path):
    result = run_smoke(ROOT / "test_section.js", tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Syntax OK: app.js" in result.stdout
    assert "Syntax OK: app.min.js" in result.stdout


@pytest.mark.parametrize("bad_runtime", ["missing", "syntax"])
def test_runtime_failure_returns_nonzero(tmp_path, bad_runtime):
    script = tmp_path / "test_section.js"
    shutil.copyfile(ROOT / "test_section.js", script)
    (tmp_path / "app.min.js").write_text("'use strict';", encoding="utf-8")
    if bad_runtime == "syntax":
        (tmp_path / "app.js").write_text("function {", encoding="utf-8")
    result = run_smoke(script, tmp_path)
    assert result.returncode != 0
    assert "app.js" in result.stderr
