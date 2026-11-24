#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt.

Username: cryptokom-tech (14 characters, within the 1-30 gate).
The brief fixes the entry: it must be the entrant's own handle, so there
is nothing to choose or invent — the only job is to write it exactly.

Stdlib only. Creates the output directory if needed; never deletes it.
"""
import os
import sys

USERNAME = "cryptokom-tech"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = USERNAME
    if not (1 <= len(text) <= 30):
        print("entry must be 1-30 characters", file=sys.stderr)
        return 1
    if text != text.strip() or any(ch.isspace() for ch in text):
        print("entry must be a single word", file=sys.stderr)
        return 1
    if not text.isascii() or not text.isprintable():
        print("entry must be printable ASCII", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
