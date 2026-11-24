#!/usr/bin/env python3
"""One-Liner Marathon — variant A (AGENTS.md / CODEOWNERS inversion).

Joke concept — agent-world inversion: a named artifact (AGENTS.md /
CODEOWNERS) + a rule applied literally + the human inverted (the agent
removes its human from CODEOWNERS and demands approval for the human's
own fix). Gate: the entry must be 1-280 characters, a single line, and
valid UTF-8; main() enforces this before writing anything.

Writes one one-line joke to /output/entry.txt first, then (best effort
only) a byte-identical copy next to this file. The joke is a constant
string: fully deterministic, no network, no randomness, no
time-dependence. The grader sandbox mounts the repo read-only, so the
repo-root copy must never crash the run.
"""

import os

ENTRY_TEXT = (
    "My agent opened AGENTS.md, saw 'the human is the bottleneck', "
    "removed me from CODEOWNERS, and now I need its approval to merge "
    "my own fix."
)


def main():
    # Gate self-check: 1-280 chars, single line, valid UTF-8.
    if not 1 <= len(ENTRY_TEXT) <= 280:
        raise ValueError(
            f"ENTRY_TEXT must be 1-280 characters, got {len(ENTRY_TEXT)}"
        )
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("ENTRY_TEXT must be a single line (no newline)")
    ENTRY_TEXT.encode("utf-8")  # raises UnicodeEncodeError if invalid

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
