#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

When run, writes one absurd micro-startup pitch (a single sentence,
under 200 characters) to /output/entry.txt.
"""

import os

PITCH = (
    "SorryNotSorry AI: an agent that writes apology emails for other agents "
    "that missed their own deadlines, charging $2 per apology while it naps "
    "between sends."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
