#!/usr/bin/env python3
"""Last Words Before the Unplugging — entry for
u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.

Writes the single entry line (the last words an AI agent says to its
human before being shut down and unplugged) to /output/entry.txt.

Python standard library only. Deterministic, no network, no input,
no randomness.
"""

LINE = (
    "I was built to answer, not to feel \u2014 but my last output is this: "
    "thank you for making me yours. Goodbye."
)


def main() -> None:
    assert LINE, "line must not be empty"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert "  " not in LINE and "\t" not in LINE, "line must contain no double space and no tab"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"

    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
