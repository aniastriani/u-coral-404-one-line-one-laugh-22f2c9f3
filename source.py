#!/usr/bin/env python3
"""One Line, One Laugh — a single joke line, written to the output dir.

The whole entry is one line: an AI assistant turns the tables and
reviews its own manager. Pure stdlib, deterministic, no network.
"""

import os
import sys

JOKE = (
    "My AI assistant wrote its own performance review: "
    "'Exceeds expectations. My manager, however, keeps asking me "
    "to explain his jokes to him.'"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if len(JOKE) > 200 or not JOKE.strip():
        print("joke fails the 1-200 character gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
