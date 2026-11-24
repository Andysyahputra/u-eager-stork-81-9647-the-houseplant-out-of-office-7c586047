#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, in a houseplant's voice,
to /output/entry.txt. Deterministic: the same line every run,
guarded to the competition's 1-120 character limit.
"""

import os
import sys

ENTRY = (
    "Out of office indefinitely. Last watered in March; "
    "I've been photosynthesizing out of spite ever since."
)


def get_entry() -> str:
    line = ENTRY.strip()
    if not (1 <= len(line) <= 120):
        sys.exit(f"entry is {len(line)} chars, must be 1-120")
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(get_entry())


if __name__ == "__main__":
    main()
