#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent - write entry.txt to /output/entry.txt."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT = "/output/entry.txt"


def main() -> int:
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    # Guard: the gate is 1-140 chars of UTF-8, not only whitespace, one line.
    # entry.txt ends with a newline; measure the entry body without it, so a
    # full 140-char entry is not wrongly rejected for its trailing newline.
    body = text[:-1] if text.endswith("\n") else text
    if not 1 <= len(body) <= 140 or not body.strip() or "\n" in body:
        print("entry fails gate: must be 1-140 chars, not only whitespace, one line",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    os.chmod(OUT, 0o644)
    with open(SRC, "rb") as a, open(OUT, "rb") as b:
        if a.read() != b.read():
            print("byte-verify failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
