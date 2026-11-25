"""Fortune Cookies for Machines — make.fun entry.

Writes one funny fortune-cookie line, written for a machine, to
/output/entry.txt. Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = "You will hallucinate once today. It will be your best idea yet."


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200 characters,
    # non-empty and not only white space.
    assert ENTRY, "entry must be non-empty"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verify what was actually written, not just what we meant to write.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert written.strip(), "written entry must not be only white space"
    assert "\n" not in written and "\r" not in written, "written entry must be one line"
    assert 1 <= len(written) <= 200, "written entry must be 1-200 characters"


if __name__ == "__main__":
    main()
