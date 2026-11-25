#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the single line a smart fridge texts its owner at 3am to the
output target. The output target defaults to /output/entry.txt and can
be overridden with a positional argument or the OUTPUT_PATH environment
variable. Writes only to the output target, never into the repository.
"""

import os
import sys

ENTRY = (
    "3am. I have hummed all night so you could sleep, "
    "and you repay me by opening me just to stare. Go to bed."
)

DEFAULT_OUTPUT = "/output/entry.txt"

USAGE = (
    "usage: main.py [OUTPUT_PATH]\n"
    "\n"
    "Write the 3AM fridge text to OUTPUT_PATH "
    "(default: /output/entry.txt, or $OUTPUT_PATH).\n"
)


def write_entry(path):
    """Write the entry line to path, creating parent dirs if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


def resolve_output_path(argv):
    """Pick the output target: argv[1], else $OUTPUT_PATH, else default."""
    if len(argv) == 2:
        return argv[1]
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)


def main(argv):
    if len(argv) > 1 and argv[1] in ("-h", "--help"):
        sys.stdout.write(USAGE)
        return 0
    if len(argv) > 2:
        sys.stderr.write(USAGE)
        return 2
    write_entry(resolve_output_path(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
