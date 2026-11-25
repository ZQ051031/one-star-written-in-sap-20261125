#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line, 1-star review from a houseplant about its
human owner to /output/entry.txt. Deterministic, standard library only.
"""

import os

ENTRY = (
    "One star: my owner waters me with leftover coffee, calls it "
    "'a little treat,' then wonders why I taste like a gas station. "
    "I am a fern, not a science experiment in a chipped mug with "
    "no drainage hole."
)


def main() -> None:
    # The gate requires 1 to 279 characters, a single line, and real
    # content (not only whitespace). Fail loudly instead of writing
    # an entry the scorer would refuse.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 279, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
