#!/usr/bin/env python
"""Wrapper script for mypy to work with lint-staged.

lint-staged appends filenames as arguments, but we want to run mypy
on the entire src/ directory for consistent type checking.
This script ignores all filename arguments and checks src/ instead.
"""

import subprocess
import sys

result = subprocess.run(
    [
        "python",
        "-m",
        "mypy",
        "src/",
        "--ignore-missing-imports",
        "--follow-imports=skip",
        "--no-incremental",
    ],
    cwd=".",
)

sys.exit(result.returncode)
