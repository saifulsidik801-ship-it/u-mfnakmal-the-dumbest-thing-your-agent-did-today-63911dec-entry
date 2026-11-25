#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — one line, max 200 chars.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os

ENTRY = "My agent spent forty minutes re-rendering a screenshot, then proudly submitted the version with the typo still in it."

assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
