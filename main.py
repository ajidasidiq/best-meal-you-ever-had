#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one original sentence (172 characters, UTF-8) about the best meal
the entrant ever had to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader). Standard library only, no network, deterministic.
"""

import os

SENTENCE = (
    "Between hotel deliveries I ate sate ayam from a cart in Menteng, "
    "smoke curling around my helmet, peanut sauce dripping down my wrist, "
    "and for once I was in no hurry at all."
)


def main() -> None:
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    # characters, not only white space, a single line, printable only.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.strip(), "sentence must not be only white space"
    assert "\n" not in SENTENCE and "\r" not in SENTENCE, (
        "sentence must be a single line"
    )
    assert SENTENCE.isprintable(), (
        "sentence must contain only printable characters"
    )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} characters to {path}")


if __name__ == "__main__":
    main()
