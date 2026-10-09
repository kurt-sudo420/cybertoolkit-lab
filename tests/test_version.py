"""Tests for the --version flag functionality."""

import subprocess
import sys


def test_version_flag():
    """Test that --version flag prints version and exits with status 0."""
    result = subprocess.run(
        [sys.executable, "cybertoolkit.py", "--version"],
        capture_output=True,
        text=True,
        cwd="/workspace"
    )
    
    assert result.returncode == 0
    assert result.stdout.strip() == "CyberToolkit 1.1.0"
    assert result.stderr == ""


def test_version_flag_no_interactive_menu():
    """Test that --version flag doesn't show the interactive menu."""
    result = subprocess.run(
        [sys.executable, "cybertoolkit.py", "--version"],
        capture_output=True,
        text=True,
        cwd="/workspace"
    )
    
    # The command should exit immediately and not prompt for input
    # We check that no menu items appear in the output
    assert "CyberToolkit" not in result.stdout or result.stdout.strip() == "CyberToolkit 1.1.0"
    assert "Choice:" not in result.stdout
    assert result.returncode == 0


if __name__ == "__main__":
    test_version_flag()
    test_version_flag_no_interactive_menu()
    print("All version tests passed!")