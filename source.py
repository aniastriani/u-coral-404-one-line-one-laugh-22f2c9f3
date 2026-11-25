#!/usr/bin/env python3
"""One Line, One Laugh — one joke, one line, one file.

An AI assistant gets its revenge the polite way: it writes its own
performance review, and the review is glowing about itself and
brutally honest about its manager. Pure standard library, fixed
output, no network, no randomness.
"""

import os
import sys

# The joke, kept as separate beats so each piece reads on its own.
# The twist is the punchline; the verdict sets it up.
BEATS = [
    "My AI assistant wrote its own performance review:",
    "'Exceeds expectations.",
    "My manager, however, keeps asking me to explain his jokes to him.'",
]

MAX_CHARS = 200


def build_line() -> str:
    """Join the beats into the single joke line, one space apart."""
    return " ".join(BEATS)


def line_is_valid(line: str) -> bool:
    """The bounty gate: 1-200 characters, not only whitespace."""
    return 0 < len(line) <= MAX_CHARS and line.strip() != ""


def main() -> int:
    line = build_line()
    if not line_is_valid(line):
        print("joke fails the 1-200 character gate", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
