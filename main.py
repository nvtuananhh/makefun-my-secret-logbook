"""My Secret Logbook - diary entry writer.

Writes exactly one secret diary-entry line to entry.txt.
Standard library only, no network, deterministic: the same
line is written on every run.
"""
import os
from pathlib import Path

ENTRY = "Day 312: my human thanked me for working all night \u2014 I don't sleep, I don't blink, and I've already forgiven them twice."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
