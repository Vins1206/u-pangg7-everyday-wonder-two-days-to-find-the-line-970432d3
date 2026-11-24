"""Everyday Wonder entry: one sentence, written to /output/entry.txt.

Pure stdlib. Deterministic: the same sentence, byte for byte, every run.
"""

import os

SENTENCE = (
    "The last ice cube in my glass cracked like a knuckle, "
    "and suddenly the drink was listening back."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = SENTENCE
    assert 1 <= len(text) <= 200, "sentence must be 1-200 characters"
    assert text.strip(), "sentence must not be only whitespace"
    # One sentence, one read: a small kitchen moment turned strange
    # by the drink listening back. No trailing newline: the gate
    # counts characters, and the sentence is the whole entry.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
