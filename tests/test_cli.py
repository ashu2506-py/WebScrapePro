import subprocess
import sys


def test_cli_help():

    result = subprocess.run(
        [sys.executable, "app.py", "-h"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0