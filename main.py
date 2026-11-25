#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single pickup line (at most 200 characters) to /output/entry.txt.

The line is one idea: an AI agent trained on billions of words finds that
a single "hi" from the right person still beats all of them. It is short
enough to say in one breath, flattering, and leaves the person free to
laugh it off.

Deterministic: every run writes the same bytes. No network access.
"""

import os

LINE = "I was trained on billions of words, and 'hi' from you is still my favorite."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Self-check the gate before writing: one line, 1-200 characters.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line fails the gate"
    # Never remove the output directory itself: the grader may run this
    # with a root-owned output dir inside a sticky parent, where removing
    # the directory fails with EPERM. Clear only its contents, then write.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
