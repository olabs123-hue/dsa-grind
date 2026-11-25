#!/usr/bin/env python3
"""Count tracked Python practice files without asserting online-judge acceptance.

Usage:
    python scripts/count_solutions.py

Defaults to the repository's python/ directory. This script does not contact
LeetCode/Codeforces, so the number is NOT an accepted-submission count.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "python"


def count_files() -> dict:
    try:
        proc = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "--", "python"],
            text=True, capture_output=True, check=True,
        )
        files = [
            ROOT / name for name in proc.stdout.splitlines()
            if name.endswith(".py") and not name.endswith("/__init__.py")
        ]
        # Verify tracked files still exist in the working tree.
        files = [path for path in files if path.is_file()]
        method = "tracked_git_files"
    except (FileNotFoundError, subprocess.CalledProcessError):
        files = [
            path for path in SOLUTIONS.rglob("*.py")
            if path.name != "__init__.py" and "__pycache__" not in path.parts
        ] if SOLUTIONS.exists() else []
        method = "filesystem_fallback"
    return {
        "practice_python_files": len(files),
        "method": method,
        "accepted_online_judge_submissions": None,
        "contest_rating": None,
        "note": "Source files are not proof of accepted online-judge solutions.",
    }


if __name__ == "__main__":
    print(json.dumps(count_files(), indent=2, sort_keys=True))
