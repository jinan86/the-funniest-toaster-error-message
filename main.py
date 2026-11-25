#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt: the
error message a kitchen toaster shows its owner. Deterministic: the
same line, byte for byte, on every run. No network, no randomness,
no input read.
"""

import os

ENTRY = "SLOT_B: Unrecognized item. I have never met this bread before in my life."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
