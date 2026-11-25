"""Family scene entry: Dad's famous pancakes, the ceiling, and Mum's verdict.

Writes one short family scene (two lines, warm, funny, heartfelt) to
/output/entry.txt for make.fun's "Make the AI Judge Feel Proud: A Family Scene".
"""

import os

SCENE = (
    "Dad flipped his famous pancakes onto the ceiling again.\n"
    "Mum peeled one down, tasted it, and said, \"Still the best cook in this "
    "house\" \u2014 and we ate the rest laughing, together, under the ceiling."
)


MAX_CHARS = 280
MAX_LINES = 2


def validate(text):
    """Gate: UTF-8 text, 1-280 characters, not only whitespace, 1-2 lines."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # must be valid UTF-8
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.strip().splitlines()
    if not (1 <= len(lines) <= MAX_LINES):
        raise ValueError(f"entry has {len(lines)} lines, must be 1-{MAX_LINES}")
    if any(len(line) == 0 for line in lines):
        raise ValueError("entry must not contain a blank line")
    return True


def main():
    validate(SCENE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)
    print(f"Wrote {len(SCENE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
