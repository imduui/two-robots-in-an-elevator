#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward small talk that one robot says to another
while riding an elevator together, to /output/entry.txt.
"""

import os

LINE = "Oh \u2014 funny running into you. My navigation said this elevator was empty."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
