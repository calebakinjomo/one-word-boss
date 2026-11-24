#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Prints exactly one word describing your boss, and writes the same word
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""
import os

WORD = "Bottleneck"


def main():
    print(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
