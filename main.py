"""Write one weird job title to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default "out"), writes the title as UTF-8
bytes with no trailing newline, then validates the written file.
Python 3.13, standard library only.
"""

import os

LINE = "Professional Mourner for Strangers"

CHAR_LIMIT = 60


def validate(path):
    """Check entry.txt: single line, 1-60 chars, no trailing newline."""
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == LINE, "content does not match LINE"
    assert 1 <= len(text) <= CHAR_LIMIT, "length must be 1-60 characters"
    assert "\n" not in text, "must be a single line"
    assert "\r" not in text, "no carriage returns allowed"
    assert not data.endswith(b"\n"), "no trailing newline allowed"
    assert text == text.strip(), "no leading or trailing whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    validate(path)


if __name__ == "__main__":
    main()
